from github_api import get_repos_from_username
from DocumentAI import scan_resume
from get_skills_resume import get_skills
from github_api import get_repos_from_username

def runPipeline(username, pdf):
    print(username)
    resume_raw_text = scan_resume(pdf.read())
    skills = get_skills(resume_raw_text)
    repos = get_repos_from_username(username)