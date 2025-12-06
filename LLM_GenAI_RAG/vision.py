import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-pro-latest")

response = model.generate_content(
    ["Explain this chart:", genai.upload_file("/Users/tayyabkhan/python/HR Analytics Dashboard.png")]
)

print(response.text)
