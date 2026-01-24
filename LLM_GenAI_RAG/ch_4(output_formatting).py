from google import genai

client=genai.Client(
    api_key="your gemini api key"
)

prompt="""
Explain RAG.
Return output strictly in JSON format.

{
  "definition": "",
  "why_used": "",
  "example": ""
}
"""

response=client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)