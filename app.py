import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------- Custom CSS --------------------------
st.markdown(
    """
    <style>
    /* Global styles */
    body {
        background-color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stApp {
        background-color: #ffffff;
    }
    /* Main header style */
    .main-header {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #2E4053;
        margin-bottom: 20px;
    }
    /* Subheader style */
    .sub-header {
        font-size: 24px;
        font-weight: 500;
        text-align: center;
        color: #34495E;
        margin-bottom: 15px;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #2C3E50;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar h2 {
        color: #ecf0f1;
        text-align: center;
        margin-bottom: 20px;
    }
    .sidebar label, .sidebar p {
        color: #bdc3c7;
    }
    /* Resume card styling */
    .resume-card {
        background-color: #ffffff;
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .resume-card h3 {
        color: #2E4053;
        margin-bottom: 10px;
    }
    .resume-card p {
        color: #7f8c8d;
        font-size: 16px;
    }
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background-color: #2980B9 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------- Sidebar --------------------------
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.markdown("<h1>Welcome</h1>", unsafe_allow_html=True)
    
    # Upload PDF resumes and job description input
    job_description = st.text_area(" Enter Job Description")
    st.markdown("<hr>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader(" Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------- Main Content --------------------------
st.markdown("<h1 class='main-header'>📄 AI Resume Screening & Ranking System</h1>", unsafe_allow_html=True)

# -------------------------- Helper Functions --------------------------
def extract_text_from_pdf(file):
    """Extracts text from each page of a PDF file."""
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

def rank_resumes(job_description, resumes):
    """Ranks resumes based on cosine similarity to the job description."""
    documents = [job_description] + resumes
    tfidf_matrix = TfidfVectorizer().fit_transform(documents)
    vectors = tfidf_matrix.toarray()
    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_vector], resume_vectors).flatten()
    return cosine_similarities

# -------------------------- Processing and Display --------------------------
if uploaded_files and job_description:
    st.markdown("<h2 class='sub-header'>🏆 Ranking Resumes</h2>", unsafe_allow_html=True)
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)
    
    # Compute similarity scores and convert them to percentages
    scores = rank_resumes(job_description, resumes) * 100
    results = pd.DataFrame({
        "Resume": [file.name for file in uploaded_files],
        "Score": scores
    }).sort_values(by="Score", ascending=False)
    
    # Highlight the best matching resume
    top_resume = results.iloc[0]
    st.success(f"🎯 Best Match: **{top_resume['Resume']}** with **{top_resume['Score']:.2f}% match!**")
    
    # Display resume cards with progress bars
    for i, row in results.iterrows():
        st.markdown(
            f"""
            <div class='resume-card'>
                <h3> {row['Resume']}</h3>
                <p>Matching Score: <b>{row['Score']:.2f}%</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(row["Score"] / 100)
    
    st.markdown("<h2 class='sub-header'> Resume Ranking Chart</h2>", unsafe_allow_html=True)
    st.bar_chart(results.set_index("Resume"))
elif not job_description:
    st.info("Please enter details in sidebar.")
elif not uploaded_files:
    st.info("Please upload at least one PDF resume.")
