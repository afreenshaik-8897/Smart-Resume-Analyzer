<<<<<<< HEAD
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
=======
import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "html", "css", "javascript", "react",
    "node", "django", "flask",
    "machine learning", "deep learning",
    "data analysis"
]

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            skills.add(skill)
    return skills

def match_job_description(resume_skills, job_description):
    job_skills = extract_skills(job_description.lower())

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills - resume_skills

    if job_skills:
        match_percentage = (len(matched_skills) / len(job_skills)) * 100
    else:
        match_percentage = 0

    return match_percentage, matched_skills, missing_skills
>>>>>>> 2a7453a101c9de90c91bde5bd4e23a1ca6932773
