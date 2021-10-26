import requests
import json
from bs4 import BeautifulSoup

def sports():
	re=requests.get("https://timesofindia.indiatimes.com/sports")
	su=BeautifulSoup(re.text,'html5lib')

	hdings1=su.findAll("div",{"class":"sports-home-videos"})

	ul=hdings1[0].find("ul")

	lis1=[]
	for x in ul:
		lis1.append(x)

	cont={}
	cnt=0
	for x in lis1:
		link=x.find("a")
		try:
			lii=[]
			s=str(cnt)
			lii.append(link.get('title'))
			lii.append(link.get('href'))
			im=link.find('img')
			lii.append(im.get('data-src'))
			cont[s]=lii
			cnt+=1
		except Exception as ee:
			print("")

	return cont

	
	


