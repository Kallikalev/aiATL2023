from github_api import get_repos_from_username
from DocumentAI import scan_resume
from get_skills_resume import get_skills
from github_api import get_repos_from_username
from RawFileToDesc import rawToDesc
from FileDescToRepoDesc import fileToRepoDesc

def runPipeline(username, pdf):
    print(username)
    resume_raw_text = scan_resume(pdf.read())
    skills = get_skills(resume_raw_text)

    repos = get_repos_from_username(username)
    for repo in repos:        
        print("Processing repository: " + repo["name"])
        print("\n")

        for file in repo["files"]:
            print("Processing file " + file["name"])
            file["description"] = rawToDesc(skills, repo["name"], repo["readme"], file["name"], file["contents"])
            print("\n")

        file_descriptions = [f["description"] for f in repo["files"]]
        repo_description = fileToRepoDesc(skills, repo["name"], file_descriptions, repo["stars"], repo["readme"], repo["primaryLanguage"])
        print(repo_description)
        print("\n")