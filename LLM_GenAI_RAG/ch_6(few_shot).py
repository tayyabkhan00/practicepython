from google import genai

client=genai.Client(
    api_key="your gemini api key"
)

prompt = """
Classify sentiment.

Example:
Text: I love this phone
Sentiment: Positive

Text: Battery is bad
Sentiment: Negative

Now classify:
Text: Camera is okay but costly
Sentiment:
"""

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)
