from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive, GoogleDriveFile
from pydrive.files import LoadMetadata
import sys
import os

# python image_downloader.py "number".jpg

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
drive_file = GoogleDriveFile(gauth)

IMG_NAME = sys.argv[1]
save_folder = './img'
print(IMG_NAME)

fid = '1-SqqFBwBaulM_ocZf8xN_56tGBZsRP9F' # reborn_01_raw
# fid = '1_P81dXHgM4KM0khFsu3GSfver0Js3G0o'

query = "'{}' in parents and trashed=false".format(fid)

for file_list in drive.ListFile({'q': query}):
    print(file_list)
    for f in file_list:
        if f['title'] == IMG_NAME:
            # f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}], 'title': IMG_NAME, 'mimeType': 'image/jpeg'})
            f.GetContentFile(os.path.join(save_folder, f['title']))

            print("Done download image")