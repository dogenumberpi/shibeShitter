import ffmpy
import httplib2
import json
import tkinter
import base64
import subprocess
import os 
import shutil
from ffmpy import FFmpeg
from PIL import Image, ImageDraw, ImageFont, ImageTk
from decimal import Decimal

print("Shibe shitter activated")
print("Cleaning directory")

for filename in os.listdir("shibes"):
    file_path = os.path.join("shibes", filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))   

x = 0
dest = 68
number = 0
while x < dest:

    x += 1
    print("on frame %d" % (x))

    h = httplib2.Http(".cache")
    (_, content) = h.request("http://shibe.online/api/shibes?count=25&urls=true&httpsUrls=false", "GET")

    decodedContent = json.loads(content, parse_float=Decimal)

    for key in decodedContent:
        number += 1

        (_, data) = h.request(key, "GET")

        with open("shibes/img%d.jpeg" % (number), 'wb') as f:
            f.write(data)
        

print("Video generating")
subprocess.call('ffmpeg.exe -r 25 -s 1024x1024 -y -i shibes/img%d.jpeg -i music.mp3 -crf 25 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" shibeShit.mp4')


