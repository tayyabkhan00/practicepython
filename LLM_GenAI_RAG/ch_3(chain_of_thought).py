from google import genai

client=genai.Client(
    api_key="your gemini api key"
)

prompt="""
Calculate EMI for a loan of 5 lakh at 8% for 20 years.
Give final EMI and a short explanation.
"""

response=client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print(response.text)
