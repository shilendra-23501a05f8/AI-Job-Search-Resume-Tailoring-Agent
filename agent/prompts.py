JOB_RELEVANCE_PROMPT = """
You are an AI job screening agent.

User skills:
{skills}

Target role:
{role}

Job description:
{job_text}

Classify the job as one of:
- Highly Relevant
- Moderately Relevant
- Not Relevant

Return ONLY the label.
"""
JOB_SCORE_PROMPT = """
You are an AI job matching agent.

User skills:
{skills}

Job description:
{job_text}

Give a relevance score from 0 to 100 based on skill match.
Respond with ONLY a number.
"""
JOB_URGENCY_PROMPT = """
You are an AI hiring urgency detector.

Job description:
{job_text}

Classify urgency as:
- High
- Medium
- Low

Respond with ONLY one word.
"""
RESUME_TAILOR_PROMPT = """
You are an expert resume writer.

Base resume:
{resume}

Job description:
{job_text}

Rewrite the resume to better match the job.
Rules:
- Do NOT add fake experience
- Rephrase skills and projects to match keywords
- Keep it concise

Return the tailored resume in plain text.
"""

COVER_LETTER_PROMPT = """
You are an expert cover letter writer.

Resume:
{resume}

Job description:
{job_text}

Write a short, professional cover letter (150-200 words).
"""
