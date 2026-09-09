from bs4 import BeautifulSoup


def parse_jobs(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    job_list = []

    for job in soup.select(".jobadentry"):
        title_elem = job.select_one(".green")
        category_elem = job.select_one(".jobadentry-category span")
        link_elem = job.find_parent("a")

        if title_elem is None:
            continue

        title = title_elem.get_text(" ", strip=True)

        category = (
            category_elem.get_text(" ", strip=True)
            if category_elem
            else None
        )

        url = link_elem.get("href") if link_elem else None

        job_list.append({
            "title": title,
            "category": category,
            "url": url,
        })

    return job_list