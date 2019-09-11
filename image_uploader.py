from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive, GoogleDriveFile
from pydrive.files import LoadMetadata
import sys

# python image_uploader.py "number".jpg

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
drive_file = GoogleDriveFile(gauth)

IMG_NAME = sys.argv[1] # "number".jpg

# f = drive.CreateFile({'title': IMG_NAME, 'mimeType': 'image/jpeg'})
# f.SetContentFile('./results/raw.jpg')
# f.SetContentFile('./results/' + 'IMG_NAME' + '.jpg')
# f.Upload()

fid = '1_P81dXHgM4KM0khFsu3GSfver0Js3G0o' #reborn_02_generated
f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}], 'title': IMG_NAME, 'mimeType': 'image/jpeg'})
f.SetContentFile('./results/' + IMG_NAME)
f.Upload()

print("Done upload image")