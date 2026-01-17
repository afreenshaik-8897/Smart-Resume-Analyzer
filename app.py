
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
import streamlit as st
from resume_parser import (
    extract_text_from_pdf,
    extract_skills,
    match_job_description
)

st.set_page_config(page_title="Smart Resume Analyzer", page_icon="📄")

st.title("📄 Smart Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_desc = st.text_area("Paste Job Description Here")

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills(resume_text)

    match_percent, matched_skills, missing_skills = match_job_description(
        resume_skills, job_desc
    )

    st.subheader(f"📊 Match Percentage: {match_percent:.2f}%")
    st.progress(int(match_percent))

    st.subheader("✅ Matched Skills")
    if matched_skills:
        for skill in matched_skills:
            st.markdown(
                f"<span style='color:green'>✔ {skill.capitalize()}</span>",
                unsafe_allow_html=True
            )
    else:
        st.write("No matched skills found")

    st.subheader("❌ Missing Skills")
    if missing_skills:
        for skill in missing_skills:
            st.markdown(
                f"<span style='color:red'>✘ {skill.capitalize()}</span>",
                unsafe_allow_html=True
            )
    else:
        st.write("No missing skills 🎉")
