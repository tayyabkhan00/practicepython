import pandas as pd
import google.generativeai as genai 
from sklearn.metrics.pairwise import cosine_similarity
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-pro-latest")

df = pd.DataFrame({
    "feedback": [
        "delivery was late",
        "great product quality",
        "customer support was slow",
        "shipping took too long"
    ]
})

# Create embeddings
df["embedding"] = df.feedback.apply(lambda x:
    genai.embed_content(model="text-embedding-004", content=x)["embedding"]
)

# Query
query = "delivery issues"
q_emb = genai.embed_content(model="text-embedding-004", content=query)["embedding"]

# Similarity
df["similarity"] = df.embedding.apply(
    lambda x: cosine_similarity([x], [q_emb])[0][0]
)

print(df.sort_values("similarity", ascending=False))
