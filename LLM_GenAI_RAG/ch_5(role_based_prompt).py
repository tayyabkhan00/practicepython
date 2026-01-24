from google import genai

client=genai.Client(
    api_key="your gemini api key"
)

prompt = """
You are a senior data scientist.
Explain RAG to a beginner with a real-world example.
"""

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)
