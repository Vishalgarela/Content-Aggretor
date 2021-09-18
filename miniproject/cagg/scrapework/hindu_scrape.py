import requests
import json
from bs4 import BeautifulSoup

re=requests.get("https://www.thehindu.com/news/national/")
su=BeautifulSoup(re.text,'html5lib')

hdings1=su.findAll("div",{"class":"33_1x_OtherStoryCard mobile-padding"})
hdings2=su.findAll("div",{"class":"tc1-slide slick-slide"})
lis1=[]
lis2=[]
print(hdings2)
for x in hdings1:
	lis1.append(x)
for x in hdings2:
	lis2.append(x)

for x in lis2:
	h5=x.find("h5")
	link=h5.find("a")
	print("link:"+link.get("href")+'\n')
	print(link.text)

for x in lis1:
	link=x.find("a")
	print(link.text+'\n')
	print(link.get("href"))