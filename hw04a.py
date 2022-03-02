"""
Provides the function get_repo_list (which
uses the GitHub API) below, and lists the
repo data along with the number of commits,
with each line following the form
Project: 5
for a repository called "Project" with 5 commits
"""
import requests


def get_repo_list(github_id):
    """
    Given a GitHub user ID with public repositories, the function
    returns an array of tuples of form (repo, n) where repo is a
    string referring to the name of the public repository and n
    is the number of commits for that repository.
    """
    repo_data = requests.get(f'https://api.github.com/users/{github_id}/repos')
    arr = []
    if repo_data:
        repo_json = repo_data.json()
        for repo in repo_json:
            repo_name = repo['name']
            commits_data = requests.get(
                f'https://api.github.com/repos/{github_id}/{repo_name}/commits')
            if commits_data:
                commits_json = commits_data.json()
                arr.append((repo_name, len(commits_json)))
            else:
                return f"Error retrieving commit data from repo '{repo_name}' with status code {repo_data.status_code}: {repo_data.reason}"
        return arr
    else:
        return f"Error retrieving repo data with status code {repo_data.status_code}: {repo_data.reason}"


if __name__ == '__main__':
    USER_ID = "amitb913"
    result = get_repo_list(USER_ID)
    if not isinstance(result, list):
        print(result)
    else:
        for repository in result:
            print(repository[0] + ":", repository[1])
