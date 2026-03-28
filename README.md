# CV Job Matcher

A web app that analyzes your CV against a job description and gives you instant, structured feedback.

## What it does

Upload your CV as a PDF, paste any job description, and get back:

- Match score (0-100)
- Your strengths for the role
- Missing skills and gaps
- Concrete recommendations
- A tailored cover letter

## Why I built it

I built this as a practical experiment with the Anthropic API. The problem is real — most people apply to jobs with a generic CV and no idea how well they actually match. This tool solves that in seconds.

## Live demo

https://cv-job-matcher-swpjjdq7ihndzobdy7yegh.streamlit.app/

## Tech stack

- Python
- Streamlit
- Anthropic Claude API
- PyPDF2

## Run locally

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Anthropic API key: `ANTHROPIC_API_KEY=your_key`
4. Run: `streamlit run app.py`