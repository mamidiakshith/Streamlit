import streamlit as st
import pdfplumber
import openai

st.set_page_config(page_title="🧠 Resume Analyzer & Career Guide", layout="centered")

st.title("📄 Smart Resume Analyzer")
st.subheader("Get career suggestions and feedback on your resume")

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key or use secrets

def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def analyze_resume(text):
    prompt = f"""
    You are a career expert. A user uploaded their resume text below.
    Analyze it and respond with:
    1. Top 3 suitable job roles.
    2. Key strengths.
    3. Skill gaps to improve.
    4. Overall suggestions.

    Resume:
    \"\"\"{text}\"\"\"
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if available
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    st.success("Resume uploaded successfully!")
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        output = analyze_resume(resume_text)
    st.markdown("### 🧾 Analysis Result")
    st.markdown(output)
else:
    st.info("Please upload a PDF resume to continue.")
