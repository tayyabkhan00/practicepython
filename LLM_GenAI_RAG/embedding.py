import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
emb_model = "models/text-embedding-004"

text = "Customer complained about slow delivery."

result = genai.embed_content(
    model=emb_model,
    content=text,
    task_type="semantic_similarity"
)

print("Embedding length:", len(result["embedding"]))
print(result["embedding"][:5])
