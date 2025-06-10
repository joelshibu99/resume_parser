import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import time

# ✅ Replace this with your working Gemini API key
genai.configure(api_key="AIzaSyCJBNlwrC3SVfIWtI-qDLzmQ6-vyanEL1w")

# You can customize the model name here
MODEL_NAME = "gemini-2.0-flash"

def parse_resume_with_gemini(text, retries=3, delay=30, model_name=MODEL_NAME):
    prompt = f"""
    Extract the following details from this resume in clean JSON format:
    - Full Name
    - Email
    - Phone
    - Skills
    - Education
    - Experience

    Resume:
    {text}
    """

    gen_model = genai.GenerativeModel(model_name)

    for attempt in range(1, retries + 1):
        try:
            response = gen_model.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            print(f"[Attempt {attempt}] Quota exceeded. Retrying in {delay} seconds...")
            time.sleep(delay)
        except Exception as e:
            print(f"[Attempt {attempt}] Unexpected error: {e}")
            break

    return '{"error": "Quota exceeded or unexpected error occurred. Please try again later."}'
