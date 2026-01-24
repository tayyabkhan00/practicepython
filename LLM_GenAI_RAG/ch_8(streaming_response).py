from google import genai

client = genai.Client(
    api_key="your gemini api_key"
)

for chunk in client.models.generate_content_stream(
    model="models/gemini-flash-latest",
    contents="Explain vector databases simply"
):
    print(chunk.text, end="")
