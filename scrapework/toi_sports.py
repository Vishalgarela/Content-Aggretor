import requests
import json
from bs4 import BeautifulSoup

re=requests.get("https://timesofindia.indiatimes.com/sports")
su=BeautifulSoup(re.text,'html5lib')

hdings1=su.findAll("div",{"class":"sports-home-videos"})

ul=hdings1[0].find("ul")

lis1=[]
for x in ul:
	lis1.append(x)


for x in lis1:
	link=x.find("a")
	try:
		print("link: "+link.get('href')+"\n")
		print(link.get('title')+"\n")
		im=link.find('img')
		print(im.get('data-src'))
		print('***'*50)
	except Exception as ee:
		print(ee)

	
	


