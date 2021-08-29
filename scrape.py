import requests
import json
from bs4 import BeautifulSoup

re=requests.get("https://timesofindia.indiatimes.com/india")
su=BeautifulSoup(re.text,'html5lib')

hdings=su.findAll("div",{"class":"items-list scroller slideshow2"})
lis=[]
for x in hdings:
	lis.append(x)

lis.pop(0)
ff=[]
for x in lis:
	ff.append(x.find('ul'))
li=[]
for x in ff:
	for y in x.contents:
		li.append(y)

ans={}
for x in li:
	link=x.find("a")
	im=link.find("img")
	ans.append({"desc":x.text,"aclink":link.get("href"),"piclink":im.get("data-src")})


with open('data.txt', 'w') as outfile:
	json.dump(ans,outfile)


#for x in hd2:
#	print(x)