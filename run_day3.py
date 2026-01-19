import json
from agent.resume_agent import tailor_resume, generate_cover_letter

# Load best job (top scored)
with open("data/jobs_day2.json", "r") as f:
    jobs = json.load(f)

if not jobs:
    print("No jobs available from Day 2. Please relax job filters.")
    exit(0)

best_job = jobs[0]


# Load base resume
with open("resume/base_resume.txt", "r") as f:
    base_resume = f.read()

print("Tailoring resume for:")
print(best_job["title"])
print(best_job["url"])

tailored_resume = tailor_resume(
    base_resume,
    best_job["snippet"]
)

cover_letter = generate_cover_letter(
    tailored_resume,
    best_job["snippet"]
)

# Save outputs
with open("resume/tailored_resume.txt", "w") as f:
    f.write(tailored_resume)

with open("resume/cover_letter.txt", "w") as f:
    f.write(cover_letter)

print("\nResume and cover letter generated successfully.")
