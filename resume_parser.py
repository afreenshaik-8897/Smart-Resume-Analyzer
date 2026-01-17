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