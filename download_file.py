import requests
import base64

def upload_file_to_github(repo_name, file_path, commit_message, branch_name):
    # קריאת הקובץ והמרתו ל-base64
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    # הגדרת הכתובת של ה-API
    url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"

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
commit_message = "Add downloaded file"
branch_name = "main"

upload_file_to_github(repo_name, file_path, commit_message, branch_name)
    url = 'https://mitmachim.top/assets/uploads/files/1586507580718-%D7%92%D7%99%D7%9E%D7%98%D7%A8%D7%99%D7%95%D7%9F-%D7%9C%D7%A9%D7%9E%D7%97%D7%95%D7%AA-1.3.rar'
    filename = "downloaded_file"
    download_file(url, filename)
