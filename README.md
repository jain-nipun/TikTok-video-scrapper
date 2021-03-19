# TikTok Video Scrapper
Created a TikTok video scrapper API to call the most trending and fetch and download the video specified by the username and hashtags. 
User is allowed to download the video and store it as a zip file.

# Requirements
Run the following commands on commandPrompt
1. pip install TikTokAPI                  
2. python -m playwright install 

Following Libraries are used
1. TikTokAPI
2. zipfile
3. sys
4. random
5. GoogleAuth
6. GoogleDrive

Google Drive Api must be configured and download json package and name it client_secrets.json

# How to Run the code
Open the terminal and type following command
1. To give username : python <filePath>TikTok-video-scrapper.py u <username>
2. To give hashtag : python <filePath>TikTok-video-scrapper.py h <hashtag>

# Extra Functionality
User is able to store the downloaded video on Google Drive also.
