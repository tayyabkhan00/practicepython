from google import genai

client=genai.Client(
    api_key="your gemini api key"
)

prompt = """
Compare RAG vs Fine-tuning.
Show output in table format with columns:
Approach | Cost | Data Update | Use Case
"""

response=client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)