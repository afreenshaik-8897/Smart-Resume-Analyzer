import spacy
from PyPDF2 import PdfReader

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Skill database
SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "html", "css", "javascript", "react",
    "node", "django", "flask",
    "machine learning", "deep learning",
    "data analysis"
]

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

def match_job_description(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description.lower())

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    return matched_skills, missing_skills