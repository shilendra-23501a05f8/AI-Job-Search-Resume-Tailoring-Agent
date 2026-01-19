import json
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")

from tools.job_search import search_jobs
from agent.prompts import (
    JOB_RELEVANCE_PROMPT,
    JOB_SCORE_PROMPT,
    JOB_URGENCY_PROMPT
)

llm = Ollama(model="llama3")

def load_user_profile():
    with open("data/user_profile.json", "r") as f:
        return json.load(f)

def agent_run():
    profile = load_user_profile()
    all_jobs = []

    for role in profile["target_roles"]:
        location = profile.get("job_preferences", {}).get("location", "India")
        jobs = search_jobs(role, location)

        # Fallback if search returns nothing
        if not jobs:
            print("No jobs from search, using seeded jobs")
            with open("data/seed_jobs.json", "r") as f:
                jobs = json.load(f)
  



        for job in jobs:
            relevance_prompt = JOB_RELEVANCE_PROMPT.format(
                skills=", ".join(profile["skills"]),
                role=role,
                job_text=job["snippet"]
            )

            relevance = llm.invoke(relevance_prompt).strip()

            score_prompt = JOB_SCORE_PROMPT.format(
                skills=", ".join(profile["skills"]),
                job_text=job["snippet"]
            )

            raw_score = llm.invoke(score_prompt).strip()
            print("  → Raw score:", raw_score)

            digits = "".join(c for c in raw_score if c.isdigit())
            score = int(digits) if digits else 0


            urgency_prompt = JOB_URGENCY_PROMPT.format(
                job_text=job["snippet"]
            )

            urgency = llm.invoke(urgency_prompt).strip()

            job.update({
                "role": role,
                "relevance": relevance,
                "score": score,   # score is already an int
                "urgency": urgency
            })


            all_jobs.append(job)

    # sort by score (high → low)
    all_jobs.sort(key=lambda x: x["score"], reverse=True)

    with open("data/jobs_day2.json", "w") as f:
        json.dump(all_jobs, f, indent=2)

    return all_jobs
print("\nAgent run completed successfully.")
