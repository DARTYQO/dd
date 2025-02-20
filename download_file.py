import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    url = "YOUR_FILE_URL_HERE"
    filename = "downloaded_file"
    download_file(url, filename)