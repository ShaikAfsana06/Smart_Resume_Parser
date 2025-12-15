import streamlit as st
from utils import *

st.set_page_config(page_title="Smart Resume Parser")

st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)", type=["pdf", "docx"]
)

job_desc = st.text_area("Paste Job Description (Optional)")

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_pdf_text(uploaded_file)
    else:
        text = extract_docx_text(uploaded_file)

    cleaned_text = clean_text(text)

    st.subheader("✅ Extracted Skills")
    st.write(extract_skills(cleaned_text))

    if job_desc:
        match_score = match_resume(cleaned_text, job_desc)
        st.subheader("📊 Job Match Score")
        st.success(f"{match_score}%")
