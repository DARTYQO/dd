import os
from github import Github

def upload_file_to_github(repo_name, file_path, commit_message, branch_name):
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token)
    repo = g.get_repo(repo_name)
    with open(file_path, 'rb') as file:
        content = file.read()
    repo.create_file(file_path, commit_message, content, branch=branch_name)

if __name__ == "__main__":
    repo_name = "YOUR_GITHUB_REPO_HERE"
    file_path = "downloaded_file"
    commit_message = "Add downloaded file"
    branch_name = "main"
    upload_file_to_github(repo_name, file_path, commit_message, branch_name)