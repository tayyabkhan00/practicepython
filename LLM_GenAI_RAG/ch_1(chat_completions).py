from google import genai

client = genai.Client(
    api_key="your gemini api key"
)

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Explain RAG in simple words"
)

print(response.text)
