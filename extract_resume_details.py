import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_details(text):
    doc = nlp(text)
    details = {"name": "", "skills": [], "education": [], "experience": []}

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            details["name"] = ent.text
        elif ent.label_ in ["ORG", "EDUCATION"]:
            details["education"].append(ent.text)

    skills_set = {"Python", "Java", "Machine Learning", "AI", "Deep Learning", "Data Science", "SQL", "NLP"}
    for token in doc:
        if token.text in skills_set:
            details["skills"].append(token.text)

    return details
