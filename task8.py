import urllib.request
import re
import os
from PIL import Image

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
dl = urllib.request.urlopen(url)

pic = dl.read()

start_dir = "./img/"

if not os.path.exists(start_dir):
    os.makedirs(start_dir)

pic_path = start_dir + "pic.png"
savedFile = open(pic_path, "wb")
savedFile.write(pic)
savedFile.close()

pic = Image.open(pic_path)

y = 0
while True:
    r, g, b, a = pic.getpixel((0, y))
    if r == g == b:
        break
    y += 1

message = ''.join([chr(pic.getpixel((x, y))[0]) for x in range(0, pic.size[0], 7)])
out = re.findall('\d+', message)

print(message)
print(''.join([chr(int(i)) for i in out]))



