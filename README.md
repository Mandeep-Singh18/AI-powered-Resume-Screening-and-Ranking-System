
# AI Resume Screening & Ranking System

## Project Description
The **AI Resume Screening & Ranking System** is an innovative web application designed to help recruiters and HR professionals streamline the resume evaluation process. By leveraging Natural Language Processing (NLP) techniques, the system extracts text from uploaded PDF resumes and compares them to a given job description. It then ranks each resume based on the cosine similarity of their textual content, displaying the results in an intuitive and visually appealing interface.

## Features
- **Resume Upload:** Easily upload multiple PDF resumes.
- **Job Description Input:** Enter a job description against which the resumes will be evaluated.
- **Automated Ranking:** Uses TF-IDF vectorization and cosine similarity to compute a match score for each resume.
- **Visual Results:** Displays match scores as percentage values with progress bars and provides a bar chart summary.
- **Attractive UI/UX:** Modern design with custom styling for a user-friendly experience.

## Requirements
The project is built using Python and requires the following libraries:
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/)

Install the dependencies using the provided `requirements.txt` file:

```
pip install -r requirements.txt

```

## Folder Structure

```
AI-powered-Resume-Screening-and-Ranking-System/
├── README.md                     
├── requirements.txt               
├── app.py                        
└── resume_ranking-checkpoint.ipynb
```
## Installation Setup

- Clone the Repository:
```
git clone https://github.com/yourusername/AI-powered-Resume-Screening-and-Ranking-System.git

cd AI-powered-Resume-Screening-and-Ranking-System
```

- Install Dependencies:
```
pip install -r requirements.txt
```

- Run the Application:
```
streamlit run app.py
```

## How It Works
- **Input Collection**: The user enters a job description and uploads one or more PDF resumes.
- **Text Extraction**: The system extracts text from each PDF using the PyPDF2 library.
- **Text Processing**: The job description and resume texts are converted into numerical features using TF-IDF vectorization.
- **Similarity Calculation**: Cosine similarity is computed between the job description and each resume to generate a matching score.
- **Result Display**: Matching scores are converted into percentages and displayed on the dashboard with progress bars, individual resume cards, and an overall bar chart visualization.
- **Feedback**: The best matching resume is highlighted, providing quick insights for recruiters.

## End User
The system is primarily designed for:

- Recruiters and HR Professionals: To streamline the initial resume screening process and identify the best candidates faster.
- Hiring Managers: To quickly assess the alignment of a candidate's resume with the job requirements.
- Job Portals and Staffing Agencies: To improve the efficiency of resume evaluation and candidate matching.

## Future Scope

- Enhanced NLP Techniques: Incorporate more advanced NLP models (such as BERT) to improve accuracy in matching resumes.
- Multi-format Support: Extend support to additional resume formats like DOCX and TXT.
- Integration with HR Systems: Connect with Applicant Tracking Systems (ATS) to automate the hiring workflow.
- Customizable Ranking Criteria: Allow users to fine-tune the ranking algorithm based on specific job requirements or candidate attributes.
- User Authentication and Data Persistence: Implement user accounts and save historical screening data for trend analysis.

## Conclusion

The AI Resume Screening & Ranking System provides a powerful, automated solution to help HR professionals and recruiters quickly identify the best candidates based on a job description. With its modern UI and robust NLP-based ranking mechanism, this project not only simplifies the resume screening process but also sets the foundation for future enhancements in candidate evaluation.
