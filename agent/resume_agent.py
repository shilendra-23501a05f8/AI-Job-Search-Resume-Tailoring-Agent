from langchain_community.llms import Ollama
from agent.prompts import RESUME_TAILOR_PROMPT, COVER_LETTER_PROMPT

llm = Ollama(model="llama3")

def tailor_resume(base_resume, job_text):
    prompt = RESUME_TAILOR_PROMPT.format(
        resume=base_resume,
        job_text=job_text
    )
    return llm.invoke(prompt)

def generate_cover_letter(resume, job_text):
    prompt = COVER_LETTER_PROMPT.format(
        resume=resume,
        job_text=job_text
    )
    return llm.invoke(prompt)
