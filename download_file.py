from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Authenticate and create the PyDrive client.
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

# Upload a file to Google Drive.
file_path = 'look'
file_drive = drive.CreateFile({'title': 'uploaded_file_name'})
file_drive.SetContentFile(file_path)
file_drive.Upload()
print('File uploaded to Google Drive')
