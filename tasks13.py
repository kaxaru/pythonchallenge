import urllib.request
import os
from PIL import Image

url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)

urllib.request.install_opener(opener)

url = urllib.request.urlopen(url)
gfx = url.read()
url.close()

start_dir = "./gfx/"

if not os.path.exists(start_dir):
	os.makedirs(start_dir)

arr = [[], [], [], [], []]
n = 0

for byte in range(len(gfx) - 1):
	arr[n].append(gfx[byte])
	n = 0 if n == 4 else n + 1

types = ['jpg','png','gif','png','jpg']

for n, elt in enumerate(arr):
	with open(start_dir + str(n+1)+'.' + types[n], 'wb') as h:
	#h = open(start_dir + str(n+1)+'.' + types[n], 'wb')
		buf = ''
		for el in elt:
			buf += chr(el)
		h.write(bytes(buf, "utf-8"))