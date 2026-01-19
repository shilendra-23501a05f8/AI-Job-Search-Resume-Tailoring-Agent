from duckduckgo_search import DDGS

# Strong signals that a page is a job posting
JOB_KEYWORDS = [
    "job", "jobs", "career", "careers",
    "apply", "hiring", "opening", "vacancy"
]

# Sites that are never job postings
BLOCKED_DOMAINS = [
    "wikipedia.org",
    "stackoverflow.com",
    "stackexchange.com",
    "zhihu.com",
    "medium.com",
    "reddit.com",
    "quora.com"
]

def is_valid_job(url: str, text: str) -> bool:
    return True


def search_jobs(role: str, location: str, max_results: int = 10):
    """
    Force known job boards for reliable results
    """
    query = (
        f"site:linkedin.com/jobs OR "
        f"site:indeed.com OR "
        f"site:internshala.com OR "
        f"site:greenhouse.io OR "
        f"site:lever.co "
        f"{role} {location}"
    )

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body", "")
            })

    return results

