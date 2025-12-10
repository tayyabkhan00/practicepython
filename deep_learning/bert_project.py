import torch
from torch.utils.data import DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from datasets import load_dataset
from tqdm import tqdm

dataset = load_dataset("imdb")

train_data = dataset["train"]
test_data = dataset["test"]

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def encode(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
        max_length=256
    )

train_enc = train_data.map(encode, batched=True)
test_enc = test_data.map(encode, batched=True)

train_enc.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])
test_enc.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

train_loader = DataLoader(train_enc, batch_size=8, shuffle=True)
test_loader = DataLoader(test_enc, batch_size=8)

model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
model = model.to("cuda")

optimizer = AdamW(model.parameters(), lr=2e-5)

epochs = 2

for epoch in range(epochs):
    model.train()
    total_loss = 0
    
    loop = tqdm(train_loader, leave=True)
    for batch in loop:
        optimizer.zero_grad()
        
        input_ids = batch["input_ids"].to("cuda")
        attention_mask = batch["attention_mask"].to("cuda")
        labels = batch["label"].to("cuda")

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )

        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        loop.set_description(f"Epoch {epoch+1}")
        loop.set_postfix(loss=loss.item())

    print(f"Epoch {epoch+1} Loss: {total_loss/len(train_loader)}")

model.eval()
correct = 0
total = 0

with torch.no_grad():
    for batch in test_loader:
        input_ids = batch["input_ids"].to("cuda")
        attention_mask = batch["attention_mask"].to("cuda")
        labels = batch["label"].to("cuda")

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        
        preds = torch.argmax(outputs.logits, dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

print("Accuracy:", correct / total)

def predict_sentiment(text):
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256)
    tokens = {key: val.to("cuda") for key, val in tokens.items()}

    with torch.no_grad():
        output = model(**tokens)
        prediction = torch.argmax(output.logits, dim=1).item()

    return "Positive" if prediction == 1 else "Negative"

print(predict_sentiment("This movie was amazing!"))
print(predict_sentiment("I hated this movie."))
