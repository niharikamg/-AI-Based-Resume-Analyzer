import streamlit as st
from resume_scoring import resume_scoring

st.title("AI-Based Resume Analyzer")

resume_text = st.text_area("Paste Resume Text Here:")
job_description = st.text_area("Paste Job Description Here:")

if st.button("Analyze"):
    score = resume_scoring(resume_text, job_description)
    st.success(f"Resume Score: {score} / 100")
