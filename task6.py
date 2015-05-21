import pickle
import urllib.request

url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

pic = pickle.load(url)
url.close()

for line in pic:
    output = ''
    for each_item in line:
      output +=each_item[0] * each_item[1]
    print(output)
