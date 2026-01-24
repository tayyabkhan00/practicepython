from google import genai

client = genai.Client(
    api_key="AIzaSyC8fBquKKPNqL9EA_QK-cL1XTB_AYn0PiY"
)

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Explain RAG in simple words"
)

print(response.text)
