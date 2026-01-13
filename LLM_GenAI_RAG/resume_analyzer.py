import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyCQOro3gTm3VeWTLVFvU3BkaLoBKqRNx5w"))
model = genai.GenerativeModel("models/gemini-pro-latest")

resume = open("resume.txt", "r").read()

response = model.generate_content(
    f"Analyze this resume and give skill gaps + improvements:\n{resume}"
)

print(response.text)
