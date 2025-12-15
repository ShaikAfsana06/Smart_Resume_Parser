Smart Resume Parser

An AI-based Smart Resume Parser that extracts key information from resumes (PDF/DOCX) and optionally matches them with job descriptions using Natural Language Processing (NLP).



 📌 Features

* Upload resumes in **PDF or DOCX** format
* Extracts **skills** from resume text
* Cleans and preprocesses resume content
* Matches resume with a **job description**
* Displays **job match percentage**
* Simple and interactive **Streamlit web interface**

---

🛠 Tech Stack
Python
spaCy (NLP)
scikit-learn(TF-IDF, Cosine Similarity)
PyMuPDF(PDF text extraction)
python-docx(DOCX text extraction)
Streamlit(Web UI)

---

📂 Project Structure

```
Smart_Resume_Parser/
│── app.py
│── utils.py
│── requirements.txt
│── README.md
│── venv/

⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Smart_Resume_Parser.git
cd Smart_Resume_Parser
```

2. Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download spaCy model:

```bash
python -m spacy download en_core_web_sm

▶️ How to Run

```bash
streamlit run app.py
```

The application will open in your browser.

📊 Output
* List of extracted skills
* Resume–Job matching score (percentage)

 🎯 Use Case
* Resume screening
* Job–candidate matching
* HR automation
* AI/NLP learning project

📄 License

This project is for learning and educational purposes.

