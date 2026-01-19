import streamlit as st
import subprocess
import os

st.set_page_config(page_title="AI Job Agent", layout="centered")

st.title("🤖 AI Job Search & Resume Tailoring Agent")
st.write("Local LLM-powered agent that finds jobs and generates tailored resumes.")

st.divider()

# ---- Day 2 ----
st.header("🔍 Step 1: Find & Rank Jobs")

if st.button("Run Job Search (Day 2)"):
    with st.spinner("Searching and ranking jobs..."):
        result = subprocess.run(
            ["python", "run_test.py"],
            capture_output=True,
            text=True
        )
    st.success("Job search completed!")
    st.text_area("Output", result.stdout, height=300)

st.divider()

# ---- Day 3 ----
st.header("📄 Step 2: Generate Resume & Cover Letter")

if st.button("Generate Resume (Day 3)"):
    with st.spinner("Generating resume and cover letter..."):
        result = subprocess.run(
            ["python", "run_day3.py"],
            capture_output=True,
            text=True
        )
    st.success("Resume generation completed!")
    st.text_area("Output", result.stdout, height=300)

st.divider()

# ---- Downloads ----
st.header("⬇️ Download Results")

resume_path = "resume/tailored_resume.txt"
cover_path = "resume/cover_letter.txt"

if os.path.exists(resume_path):
    with open(resume_path, "r", encoding="utf-8") as f:
        st.download_button(
            "Download Tailored Resume",
            f.read(),
            file_name="tailored_resume.txt"
        )

if os.path.exists(cover_path):
    with open(cover_path, "r", encoding="utf-8") as f:
        st.download_button(
            "Download Cover Letter",
            f.read(),
            file_name="cover_letter.txt"
        )
