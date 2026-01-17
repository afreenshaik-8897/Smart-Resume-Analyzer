import streamlit as st
from resume_parser import (
    extract_text_from_pdf,
    extract_skills,
    match_job_description
)

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

st.title("📄 Smart Resume Analyzer 🚀")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills(resume_text)

    st.subheader("✅ Skills Found in Resume")
    st.write(resume_skills)

    if job_description:
        matched, missing = match_job_description(resume_text, job_description)

        st.subheader("🎯 Matched Skills")
        st.write(matched)

        st.subheader("❌ Missing Skills")
        st.write(missing)