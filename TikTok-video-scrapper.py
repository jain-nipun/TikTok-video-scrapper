from TikTokApi import *
import time, sys, os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import random
import zipfile


def zipdir(path, ziph):
    # Function to Zip the folder
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def gdrive_upload(string):
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    file2 = drive.CreateFile()
    file2.SetContentFile(string)
    file2.Upload()


api = TikTokApi().get_instance(custom_verifyFp=os.environ.get('verifyFp', None))
did = str(random.randint(1000, 999999999))

results = 10
vid = ""
username = ""
trending = ""
if sys.argv[1] == "u":
    username = sys.argv[2]
    trending = api.byUsername(username, did=did, custom_verifyFp = 'your_verify_fp')[0]# count=results)
elif sys.argv[1] == "h":
    username = sys.argv[2]
    trending = api.byHashtag(username, did=did, custom_verifyFp = 'your_verify_fp')[0]#count=results)

# creates new directory
if not os.path.isdir(username):
    os.mkdir(username)

video_name = "_video.mp4"
count = 0
for tiktok in trending:
    # Prints the text of the tiktok
    count += 1
    if count % 10 == 0:
        print("Please wait for 10 sec to continue....")
        time.sleep(10)
    if sys.argv[1] == "u":
        vid = tiktok['id']
    elif sys.argv[1] == "h":
        vid = tiktok['itemInfos']["id"]
    url = 'https://www.tiktok.com/@' + username + '/video/' + vid + '?lang=en'
    print("Downloaded: " + str(count))
    # Below is used if you want no watermarks
    video_data = api.get_Video_No_Watermark(url, return_bytes=1)
    with open(username + "/" + vid + "_" + username + video_name, 'wb') as output:
        output.write(video_data)


zip_file = zipfile.ZipFile(username + '.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(username + "/", zip_file)
zip_file.close()
gdrive_upload(username + '.zip')
