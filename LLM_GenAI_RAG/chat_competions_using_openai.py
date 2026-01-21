from openai import OpenAI

client = OpenAI()
# client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":"Hello!"}]
)

print(response.choices[0].message["content"])




