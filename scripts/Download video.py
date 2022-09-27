import os
import urllib.parse as urlparse
from urllib.parse import parse_qs

url = input("Enter URL of video to download: ") 

#url = "https://www.youtube.com/watch?v=60YuPTnT_NI&list=PLA8itan-O-KdBNmIfi6JlIVVKJR_HTcfT&index=37"

parsed = urlparse.urlparse(url)

video = parse_qs(parsed.query)['v'][0]

#command = 'python -m youtube_dl -o "C:\\Users\\Nick\\Videos\\%(title)s.%(ext)s" ' + video
command = 'python -m youtube_dl -o "\\\\pikes-surfacebook\\Youtube videos\\%(title)s.%(ext)s" ' + video
 
 
#\\pikes-surfacebook\Youtube videos

print (command)

os.system(command)









