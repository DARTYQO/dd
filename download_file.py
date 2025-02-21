import requests
import base64
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def upload_file_to_github(repo_name, file_path, commit_message, branch_name):
    # קריאת הקובץ והמרתו ל-base64
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    # הגדרת הכתובת של ה-API עם תיקיית המשנה 'downloads'
    url = f"https://api.github.com/repos/{repo_name}/contents/downloads/{file_path}"

    # הגדרת הכותרות והנתונים של הבקשה
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "message": commit_message,
        "content": content,
        "branch": branch_name
    }

    # שליחת הבקשה
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()

    print("File uploaded successfully")

# דוגמה לשימוש בפונקציה
repo_name = "DARTYQO/dd"
file_path = "downloaded_file"
commit_message = "Add downloaded file to downloads folder"
branch_name = "main"

upload_file_to_github(repo_name, file_path, commit_message, branch_name)
