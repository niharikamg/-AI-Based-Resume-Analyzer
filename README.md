# AI-Based Resume Analyzer

## Features
- **Extracts Name, Skills, Education, and Experience** from resumes.
- **Matches resumes against job descriptions** using NLP & ML.
- **Generates an AI-powered Resume Score**.
- Supports **PDF & DOCX resumes**.
- Provides **Flask API & Streamlit Web UI**.

## Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
2. Extract text from resumes:
   ```
   python extract_resume_text.py
   ```
3. Extract resume details:
   ```
   python extract_resume_details.py
   ```
4. Match resume with job description:
   ```
   python match_resume.py
   ```
5. Generate resume score:
   ```
   python resume_scoring.py
   ```
6. Start the Flask API:
   ```
   python flask_api.py
   ```
7. Run the Streamlit UI:
   ```
   python streamlit_ui.py
   ```

🚀 **Now you can analyze and score resumes with AI!** 🎯
