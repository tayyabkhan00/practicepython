# gemini pro chat completion example
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-pro-latest")

response = model.generate_content("Give 5 insights from sales data.")
print(response.text)


# open ai chat completion example
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {"role": "user", "content": "Explain what EMI is in simple words"}
    ]
)

print(response.choices[0].message.content)
