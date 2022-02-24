import requests
import json

def get_repo_list(ID):
    repo_data = requests.get(f'https://api.github.com/users/{ID}/repos')
    arr = []
    if repo_data:
        repo_json = repo_data.json()
        for repo in repo_json:
            repo_name = repo['name']
            commits_data = requests.get(
                f'https://api.github.com/repos/{ID}/{repo_name}/commits')
            if commits_data:
                commits_json = commits_data.json()
                arr.append((repo_name, len(commits_json)))
            else:
                return f"Error retrieving commit data from repo '{repo_name}' with status code {repo_data.status_code}: {repo_data.reason}"
        return arr
    else:
        return f"Error retrieving repo data with status code {repo_data.status_code}: {repo_data.reason}"

if __name__ == '__main__':
    userId = "nickopicz"
    result = get_repo_list(userId)
    if not isinstance(result, list):
        print(result)
    else:
        for repo in result:
            print(repo[0] + ":", repo[1])
