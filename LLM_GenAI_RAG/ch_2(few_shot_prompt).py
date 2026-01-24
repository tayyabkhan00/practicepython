from google import genai

client = genai.Client(
    api_key="your gemini api key"
)

prompt = """
You are an AI teacher.
Explain concepts in simple Hindi-English.
Keep it short.

Question:
What is RAG?
"""

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)
