import PyPDF2
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-pro-latest")

reader = PyPDF2.PdfReader("/Users/tayyabkhan/python/report.pdf")
text = "".join(page.extract_text() for page in reader.pages)

response = model.generate_content(
    f"Summarize this report and give 10 insights:\n{text}"
)

print(response.text)
