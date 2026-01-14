import streamlit as st
import requests
from PyPDF2 import PdfReader

# --- configuration ---

resume_analyse_url = "http://localhost:8000/processing/calculate_resume_results"

# ---------------------



st.set_page_config(page_title="Home")

st.title("Resume & Job Description Processor")

# Upload resume (PDF only)
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Input job description
job_description = st.text_area("Enter Job Description")

# Submit button
if st.button("Analyse Resume"):
    if resume_file is None:
        st.error("Please upload a resume PDF.")
    elif job_description.strip() == "":
        st.error("Please enter a job description.")
    else:
        # Read PDF and convert to readable string
        reader = PdfReader(resume_file)
        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() + "\n"

        # Call API
        api_url = resume_analyse_url
        payload = {
            "resume_text": resume_text,
            "job_desc_text": job_description
        }

        print(f"resume_text: {resume_text[:100]}\n\n")
        print(f"job_dec_text: {job_description[:100]}\n\n")

        response = requests.post(
            api_url, 
            json={
                
                "resume_text": resume_text,
                "job_desc_text": job_description
            }
        )

        if response.status_code == 200:
            # Save API response to session state
            st.session_state.api_response = response.json()
            # Navigate to output page
            st.switch_page(r'pages\output.py')
        else:
            st.error("API call failed.")
