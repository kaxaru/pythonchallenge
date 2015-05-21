import urllib.request
import os
from PIL import Image

url = "http://www.pythonchallenge.com/pc/return/cave.jpg"

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)

urllib.request.install_opener(opener)

url = urllib.request.urlopen(url)
pic = url.read()

start_dir = "./img/"

if not os.path.exists(start_dir):
	os.path.makedir(start_dir)

pic_path = start_dir + "chapter11.jpg"
savedFile = open(pic_path, "wb")
savedFile.write(pic)
savedFile.close()

img = Image.open(pic_path, 'r')
nsize = tuple([int(x/2) for x in img.size])
odd = even = Image.new(img.mode, nsize)

for x in range(img.size[0]):
	for y in range(img.size[1]):
		if x % 2 == 0 and y % 2 == 0:
			even.putpixel(( int(x/2), int(y/2)), img.getpixel((x, y)))
		elif x % 2 == 0 and y % 2 == 1:
			odd.putpixel((int(x/2), int((y - 1)/2)), img.getpixel((x, y)))
		elif x % 2 == 1 and y % 2 == 0:
			even.putpixel((int((x - 1)/2), int(y/2)), img.getpixel((x, y)))
		else:
			odd.putpixel((int((x - 1) / 2), int((y - 1) / 2)), img.getpixel((x, y)))

even.save(start_dir + "even.jpg")
odd.save(start_dir + "odd.jpg")