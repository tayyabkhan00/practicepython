import google.generativeai as genai

genai.configure(api_key="AIzaSyCQOro3gTm3VeWTLVFvU3BkaLoBKqRNx5w")
model = genai.GenerativeModel("models/gemini-pro-latest")
response = model.generate_content("Give 5 insights from sales data.")
print(response.text)


