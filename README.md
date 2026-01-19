# 🤖 AI Job Search & Resume Tailoring Agent (Local LLM)

An autonomous AI agent that searches for jobs, ranks them by relevance and urgency, and automatically generates tailored resumes and cover letters using a local LLM (Ollama).  
Includes a Streamlit UI for one-click demo usage.

---

## 🚀 Project Overview

This project demonstrates how to build a real-world AI agent that:

- Searches for relevant job postings
- Evaluates each job using an LLM
  - Relevance classification
  - Numeric scoring
  - Urgency detection
- Ranks jobs automatically
- Generates a job-specific resume
- Generates a customized cover letter
- Uses fallback logic when job search fails

All intelligence runs locally — no paid APIs.

---

## 🧠 Why This Is an AI Agent (Not Just AI)

This system qualifies as an AI agent because it:

- Makes autonomous decisions (job ranking & selection)
- Uses tools (job search, resume generation)
- Maintains structured memory (user_profile.json)
- Handles failures gracefully (seeded job fallback)
- Produces actionable outputs, not just text

---

## 🏗️ Architecture

User Profile (JSON)  
↓  
Job Search Tool  
↓  
Job Intelligence Agent  
(Relevance • Score • Urgency)  
↓  
Ranked Jobs  
↓  
Resume Tailoring Agent  
↓  
Tailored Resume + Cover Letter  

---

## 📁 Project Structure

job_agent/  
├── agent/  
│   ├── agent_core.py  
│   ├── resume_agent.py  
│   └── prompts.py  
├── tools/  
│   └── job_search.py  
├── data/  
│   ├── user_profile.json  
│   ├── seed_jobs.json  
│   └── jobs_day2.json  
├── resume/  
│   ├── base_resume.txt  
│   ├── tailored_resume.txt  
│   └── cover_letter.txt  
├── app.py  
├── run_test.py  
├── run_day3.py  
├── requirements.txt  
└── README.md  

---

## ⚙️ Tech Stack

- Python 3.10+
- Ollama (Local LLM runtime)
- LangChain
- DuckDuckGo Search
- Streamlit
- JSON-based agent memory

---

## 🛠️ Setup Instructions

### 1) Install Ollama

Download from:  
https://ollama.com

Pull a model:

ollama pull llama3

---

### 2) Install Python Dependencies

pip install -r requirements.txt

---

## ▶️ How to Run (CLI)

### Day 2 — Job Intelligence

python run_test.py

Output:
- Job relevance
- Scores
- Urgency
- Ranked results

---

### Day 3 — Resume Generation

python run_day3.py

Generates:
- resume/tailored_resume.txt
- resume/cover_letter.txt

---

## 🖥️ Streamlit UI (Demo Mode)

Run:

streamlit run app.py

### UI Features

- One-click job search (Day 2)
- One-click resume generation (Day 3)
- Output logs displayed
- Download resume & cover letter

---

## 🛡️ Fallback Strategy (Important Design)

Job search engines may return zero usable results.

This agent uses a fallback mechanism:

Search Jobs → If empty → Use Seeded Jobs

This ensures:
- Reliability
- Testability
- Decoupling intelligence from data sources

This is a real-world engineering pattern.

---

## 🎯 Example Results

- 6 jobs processed
- Best job selected automatically
- Resume tailored to job description
- Cover letter generated
- Fully local execution

---

## 🗣️ Interview Explanation (Short)

“I built a local AI agent that autonomously finds jobs, ranks them by relevance and urgency, and generates job-specific resumes and cover letters. The system includes fallback strategies to handle unreliable data sources, making it robust and production-oriented.”

---

## 🔮 Future Improvements

- PDF resume generation
- Multi-job batch processing
- Interview Q&A agent
- Chrome autofill assistant
- Streamlit Cloud deployment

---

## 👤 Author

Jaya Krishna  
Aspiring Software / Backend Engineer  

---

## ⭐ If You Like This Project

Star the repository and feel free to fork or extend it.
