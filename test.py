import google.generativeai as genai

genai.configure(api_key="AIzaSyCJBNlwrC3SVfIWtI-qDLzmQ6-vyanEL1w")  # <- 👈 paste your valid Gemini API key

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Capital of France?")
print(response.text)
