import streamlit as st
import anthropic
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an expert career consultant and HR specialist. 
When analyzing a CV against a job description, you provide honest, structured, actionable feedback.
Always respond in this exact format:

## Match Score: X/100

## Your Strengths for This Role
- List what matches well

## Missing Skills or Gaps
- List what's missing or weak

## Recommendations
- Concrete actions to improve the application

## Tailored Cover Letter
Write a professional, specific cover letter based on the CV and job description."""

st.set_page_config(page_title="CV Job Matcher", page_icon="🎯", layout="wide")
st.title("🎯 CV Job Matcher")
st.write("Upload your CV and paste a job description to get an instant match analysis.")

with st.sidebar:
    st.header("How it works")
    st.markdown("""
    1. Upload your CV as PDF
    2. Paste the job description
    3. Click Analyze
    4. Get your match score, gaps, and a tailored cover letter
    """)
    st.divider()
    st.info("Your CV is never stored. Analysis happens in real time.")

st.subheader("Your CV")
uploaded_file = st.file_uploader("Upload CV (PDF)", type="pdf")
cv_text = ""
if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        cv_text += page.extract_text()
    st.success(f"CV loaded - {len(pdf_reader.pages)} page(s)")

st.subheader("Job Description")
job_description = st.text_area("Paste the job description here", height=300)

if st.button("Analyze Match", use_container_width=True):
    if not cv_text:
        st.warning("Please upload your CV.")
    elif not job_description:
        st.warning("Please paste a job description.")
    else:
        with st.spinner("Analyzing your profile against the role..."):
            try:
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2000,
                    system=SYSTEM_PROMPT,
                    messages=[
                        {
                            "role": "user",
                            "content": f"CV:\n{cv_text}\n\nJob Description:\n{job_description}"
                        }
                    ]
                )
                result = response.content[0].text
                st.markdown(result)
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")