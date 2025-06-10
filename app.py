from flask import Flask, render_template, request
from resume_parser import parse_resume_with_gemini
import PyPDF2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['resume']
        if file.filename.endswith('.pdf'):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Extract text from PDF
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

            result = parse_resume_with_gemini(text)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
