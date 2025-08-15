import streamlit as st
import PyPDF2
import os
import io
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="centered")
st.title("AI Resume Analyzer")
st.markdown("Upload your resume in PDF or TXT format to get feedback and suggestions for improvement.")

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload Your Resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for", placeholder="e.g., Software Engineer")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        return None

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read.")
            st.stop()

        prompt = f"""
        Please analyze this resume and provide constructive feedback and suggestions for improvement.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Formatting and structure
        4. Experience descriptions
        5. Specific improvements for the job role: {job_role if job_role else "General job applications"}
        
        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with bullet points and specific recommendations.
        """

        # Generate response from Gemini
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        # Display results
        st.markdown("### Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred while processing the resume: {e}")
