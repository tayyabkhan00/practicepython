import os
from google import genai
import numpy as np
import faiss

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

texts = [
    "RAG helps LLMs answer using external data",
    "Vector databases store embeddings",
    "FAISS is a fast similarity search library"
]

response = client.models.embed_content(
    model="models/text-embedding-004",
    contents=texts
)

embeddings = np.array([e.values for e in response.embeddings])

print(embeddings.shape)  # (3, embedding_dimension)


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Total vectors stored:", index.ntotal)

query = "What is a vector database?"

query_embedding = client.models.embed_content(
    model="models/text-embedding-004",
    contents=query
)

query_vector = np.array([query_embedding.embeddings[0].values])

D, I = index.search(query_vector, k=2)

print("Best matches:", I)

for i in I[0]:
    print(texts[i])


"""
PDF / Text Files
   ↓
Chunk text
   ↓
Create embeddings (Gemini)
   ↓
Store in FAISS
   ↓
User question → embedding
   ↓
Similarity search
   ↓
Send relevant text to LLM

"""