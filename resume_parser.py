
import spacy
from PyPDF2 import PdfReader

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Skill database
SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "html", "css", "javascript", "react",
    "node", "django", "flask",
    "machine learning", "deep learning",
    "data analysis"
]

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text.lower()

# Extract skills from text
def extract_skills(text):
    found_skills = set()  # Use set for easy intersection/difference
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)
    return found_skills  # return as set

# Match resume skills with job description
def match_job_description(resume_text, job_description):
    # Extract skills from resume and job description
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description.lower())

    # Calculate matched and missing skills
    matched_skills = resume_skills & job_skills       # set intersection
    missing_skills = job_skills - resume_skills      # set difference

    # Optional: calculate match percentage
    match_percentage = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

    return match_percentage, matched_skills, missing_skills

