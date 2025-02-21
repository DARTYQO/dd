import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    url = 'https://mitmachim.top/assets/uploads/files/1586507580718-%D7%92%D7%99%D7%9E%D7%98%D7%A8%D7%99%D7%95%D7%9F-%D7%9C%D7%A9%D7%9E%D7%97%D7%95%D7%AA-1.3.rar'
    filename = "downloaded_file"
    download_file(url, filename)
