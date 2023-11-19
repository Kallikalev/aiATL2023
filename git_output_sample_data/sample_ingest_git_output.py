from json_nico import test_dict
import json
 
git_dict = test_dict

for repo in git_dict:
    readme = repo["readme"] or "None found"
    stars = repo["stars"] or "None found"
    repo_name = repo["name"] or "None found"
    primaryLanguage = repo["primaryLanguage"] or "None found"
    for file in repo["files"]:
        file_language = file["language"] or "None found"
        file_name = file["name"]
        file_content = file["contents"]
    break


output = {"repo":{"file_name":file_name,
                  "file_language":file_language,
                  "file_content":file_content},
          "repo_name":repo_name,
          "repo_readme":readme,
          "stars":stars,
          "primaryLanguage":primaryLanguage}

        
with open('git_output_test.json','w') as f:
    json.dump(output,f)
