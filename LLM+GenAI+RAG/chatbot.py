import google.generativeai as genai
import pandas as pd
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-pro-latest")

df = pd.read_csv("/Users/tayyabkhan/Downloads/sales_data_sample.csv", encoding='latin1')

question = "Which region has highest revenue?"

response = model.generate_content(
    f"Answer this using the dataset:\n{df.head().to_string()}\nQuestion: {question}"
)

print(response.text)
