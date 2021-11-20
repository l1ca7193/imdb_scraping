import re

urls1 = []
urls2 = []
with open("imdb_urls.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		url = line.strip()
		code = re.findall("nm\d{1,7}",url)
		try:
			print(code[0])
			urls1.append(code[0])
		except:
			pass
print ("codiciRegisti.txt")
with open("codiciRegisti.txt", "r") as ff:
	lines = ff.readlines()
	for line in lines:
		url = line.strip()
		print(url)
#s = set(urls1)
#urls3 = [x for x in urls2 if x not in s]
#print(urls3)

#for i in urls3:
#	print(i)
