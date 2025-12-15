import fitz
import docx
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "java", "sql", "html", "css",
    "javascript", "machine learning", "data analysis",
    "flask", "django"
]

def extract_pdf_text(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_docx_text(file):
    doc = docx.Document(file)
    return " ".join(p.text for p in doc.paragraphs)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9., ]', '', text)
    return text.lower()

def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]

def match_resume(resume_text, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)
