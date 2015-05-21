str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#str = "http://www.pythonchallenge.com/pc/def/map.html"
l = list(str)
newL = list()
offset = ord('z') - ord('a')
for ch in l:
	if  ord('z') >= ord(ch) >= ord('a'):
		ch = ord(ch) + 2
		if ch > ord('z'):
			ch = ch - offset - 1
		ch = chr(ch)
	newL.append(ch)

arr = ''.join(newL).split('.')
for el in arr:
	print(el +'\n')


