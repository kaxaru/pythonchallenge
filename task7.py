import zipfile
import urllib
import re
import os

file_num = "90052"
comments = []

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
dl = urllib.request.urlopen(url)
zip = dl.read()

start_dir = "./zip/"

try:
    os.makedirs(start_dir)
except OSError:
    pass

savedFile = open(start_dir + "file.zip", 'wb')
savedFile.write(zip)
savedFile.close()

myUnZip = zipfile.ZipFile(start_dir + "file.zip")
new_path = start_dir + "zip_staff"
if not os.path.exists(new_path):
    os.makedirs(new_path)

for name in myUnZip.namelist():
    uncompressed = myUnZip.read(name)
    savedFile = open(new_path + "/" + name, 'wb')
    savedFile.write(uncompressed)
    savedFile.close()

while file_num is not "":
    file_content = open(new_path + "/" + file_num + ".txt", 'r')
    file_text = file_content.read()
    listOfNums = re.findall("\d+", str(file_text))
    for el in listOfNums:
        file_num = el
    if ((len(listOfNums) is not 0) and (file_num is not 90052) and (file_num is not "")):
        comments.append(myUnZip.getinfo(file_num + ".txt").comment)
    else:
        break


print(file_text)

output = ''

for ch in comments:
    output += ch.decode("utf-8")

print(output)
