import pandas as pd

df = pd.read_csv("file.csv")
summary = genai.GenerativeModel("gemini-2.0-flash").generate_content(
    f"Summarize this dataset and give 5 insights: {df.head().to_string()}"
).text

print(summary)