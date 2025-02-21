from extract_resume_details import extract_resume_details
from match_resume import match_resume_to_job

def resume_scoring(resume_text, job_desc):
    details = extract_resume_details(resume_text)
    match_score = match_resume_to_job(resume_text, job_desc)

    experience_score = min(len(details["experience"]) * 10, 30)
    skills_score = min(len(details["skills"]) * 10, 40)
    relevance_score = match_score * 0.3

    total_score = experience_score + skills_score + relevance_score
    return round(total_score, 2)
