import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
val = "82682"
r = range(400)
for i in r:
    text = urllib.request.urlopen(url+val).read()
    try:
      val = (re.findall("nothing is (\d+)",str(text)))[0]
      print('the next is snothing: ', val)
    except:
        print('Last: ', text)
        break
