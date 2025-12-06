import google.generativeai as genai
genai.configure(api_key="YOUR_KEY")
import faiss
import numpy as np

# step :1
# Load docs
docs = [
    "Delivery was slow.",
    "Customers liked the product quality.",
    "Support team was quick.",
    "Shipping took 10 days."
]


# step :2
# Generate embeddings
def embed_text(text):
    return genai.embed_content(
        model="text-embedding-004",
        content=text
    )["embedding"]

embeddings = [embed_text(d) for d in docs]


# step :3
# Store in FAISS
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
#  L2 → uses Euclidean distance to compare vectors → simple index, no training
# dimension → tells FAISS each vector has this many numbers
index.add(np.array(embeddings).astype('float32')) 

# step :4 
# Query
query = "delivery issues"
q_emb = np.array([embed_text(query)]).astype('float32')

distance, position = index.search(q_emb, 2)
print("Matches:", position)


# step :5 Send retrieved docs to Gemini

model = genai.GenerativeModel("gemini-2.0-pro")

context = "\n".join([docs[i] for i in position[0]])

response = model.generate_content(
    f"Using this data:\n{context}\n\nAnswer: What issues are customers facing?"
)

print(response.text)
