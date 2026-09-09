from parser import parse_jobs


def test_parse_one_job():
    html="""
    <a href="https://example.com/job">
        <div class="jobadentry">
            <div class="jobadentry-category">
                <span>Werkstudentstelle</span>
            </div>

            <div class="jobadentry-content">
                <span class="green">Python Werkstudent</span>
            </div>
        </div>
    </a>
    """

    jobs = parse_jobs(html)

    assert len(jobs) == 1
