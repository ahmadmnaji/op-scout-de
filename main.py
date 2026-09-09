import requests
from parser import parse_jobs

URL = "https://www.tu-chemnitz.de/career-service/jobboerse/"


def main():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    jobs = parse_jobs(response.text)
    print(jobs)


if __name__ == "__main__":
    main()