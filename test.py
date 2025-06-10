import google.generativeai as genai

genai.configure(api_key="API_KEY_HERE")

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Capital of France?")
print(response.text)
