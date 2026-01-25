from google import genai
import numpy as np
import faiss

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

documents = [
    "RAG helps large language models use external knowledge.",
    "FAISS is a library for efficient similarity search.",
    "Gemini provides fast and scalable LLM APIs.",
    "Vector databases store embeddings for semantic search."
]


embed_response = client.models.embed_content(
    model="models/text-embedding-004",
    contents=documents
)

embeddings = np.array([e.values for e in embed_response.embeddings])


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Vectors stored:", index.ntotal)

user_query = "What is RAG and why is it useful?"

query_embedding = client.models.embed_content(
    model="models/text-embedding-004",
    contents=user_query
)

query_vector = np.array([query_embedding.embeddings[0].values])

D, I = index.search(query_vector, k=2)


retrieved_docs = [documents[i] for i in I[0]]

context = "\n".join(retrieved_docs)

print("Retrieved context:")
print(context)


prompt = f"""
You are an AI assistant.
Answer ONLY using the context below.
If answer is not present, say "I don't know".

Context:
{context}

Question:
{user_query}
"""


for chunk in client.models.generate_content_stream(
    model="models/gemini-flash-latest",
    contents=prompt
):
    print(chunk.text, end="")


