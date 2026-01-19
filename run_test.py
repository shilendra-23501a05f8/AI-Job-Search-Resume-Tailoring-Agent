
from agent.agent_core import agent_run

results = agent_run()

print("\n=== FINAL RESULTS ===\n")

for job in results:
    print("Title:", job.get("title"))
    print("Role:", job.get("role"))
    print("Relevance:", job.get("relevance"))
    print("Score:", job.get("score"))
    print("Urgency:", job.get("urgency"))
    print("Link:", job.get("url"))
    print("-" * 60)

print(f"\nTotal jobs processed: {len(results)}")
