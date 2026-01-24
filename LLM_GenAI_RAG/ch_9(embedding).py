import os
from google import genai
import numpy as np

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
