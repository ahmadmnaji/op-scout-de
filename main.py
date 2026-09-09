import requests
from bs4 import BeautifulSoup
import pprint


URL="https://www.tu-chemnitz.de/career-service/jobboerse/"


response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.select(".jobadentry")


job_list = []
for job in jobs:
    title = job.select_one(".green").get_text(strip=True)
    category = job.select_one(".jobadentry-category span").get_text(strip=True)
    url = job.parent["href"]
    job_list.append({"title": title, "category": category, "url": url}) 


pprint.pprint(job_list)