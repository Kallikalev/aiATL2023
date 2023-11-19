import requests
import github_key

base_url = "https://api.github.com/graphql"

allowedExtensions = [".py", ".cpp", ".rs"]

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "accept": "application/vnd.github+json",
    "authorization": "token " + github_key.key
}

request_body = """
{{
  user(login: "{username}") {{
    repositories(last: 10, isFork: false) {{
        nodes {{
            name
            stargazerCount
          	defaultBranchRef {{
              target {{
                ... on Commit {{
                  history(first:1){{
                    edges{{
                      node{{
                        tree{{
                          entries {{
                          	name
                          	type
                            extension
                            language {{
                              name
                            }}
                            object {{
                              ... on Blob {{
                                text
                              }}

                              ... on Tree {{
                                entries {{
                                  name
                                  type
                                  extension
                                  language {{
                                    name
                                  }}
                                  
                                  object {{
                                    ... on Blob {{
                                      byteSize
                                      text
                                      isBinary
                                    }}
                                    
                                    ... on Tree {{
                                      entries {{
                                        name
                                        type
                                        extension
                                        language {{
                                          name
                                        }}
                                        
                                        object {{
                                          ... on Blob {{
                                            byteSize
                                            text
                                            isBinary
                                          }}
                                        }}
                                      }}
                                    }}
                                  }}
                                }}
                              }}
                            }}

                          }}
                        }}
                      }}
                    }}
                  }}
                }}
              }}
            }}
          	owner {{
          	  login
          	}}
          	primaryLanguage {{
          	  name
          	}}
        }}
    }}
  }}
}}
"""

def run_query(username):
    response = requests.post(url=base_url, json={"query": request_body.format(username=username)}, headers=headers)
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        response_json = response.json()
        return response_json

def extract_repositories(query_response):
    parsedRepositories = list()
    for repository in query_response["data"]["user"]["repositories"]["nodes"]:
        parsedFiles = list()
        primaryLanguage = None
        if repository["primaryLanguage"] is not None:
            primaryLanguage = repository["primaryLanguage"]["name"]

        newRepository = {
            "name": repository["name"],
            "files": list(),
            "primaryLanguage": primaryLanguage,
            "stars": repository["stargazerCount"],
            "readme": None
        }

        treeEntries = repository["defaultBranchRef"]["target"]["history"]["edges"][0]["node"]["tree"]["entries"]
        for entry in treeEntries:
            recursive_extract_files(entry, newRepository)

        parsedRepositories.append(newRepository)
    return parsedRepositories

def recursive_extract_files(entry, repository):
    if entry["type"] == "blob":
        if entry["name"].split(".")[0].lower() == "readme":
            repository["readme"] = entry["object"]["text"]
            return
        if "extension" in entry.keys() and entry["extension"] in allowedExtensions:
            language = None
            if entry["language"] is not None:
                language = entry["language"]["name"]
            repository["files"].append({
                "name" : entry["name"],
                "language": language,
                "contents": entry["object"]["text"]
            })
    elif entry["type"] == "tree":
        if "entries" in entry["object"]:
            for subEntry in entry["object"]["entries"]:
                recursive_extract_files(subEntry, repository)

def get_repos_from_username(username):
    return extract_repositories(run_query(username))