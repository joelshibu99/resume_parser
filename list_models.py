import google.generativeai as genai

genai.configure(api_key="API_KEY_HERE")

models = genai.list_models()
for model_info in models:
    print(model_info.name)
