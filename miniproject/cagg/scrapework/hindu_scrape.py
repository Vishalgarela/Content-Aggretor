import requests
import json
from bs4 import BeautifulSoup


def hindu():
	re=requests.get("https://www.thehindu.com")
	su=BeautifulSoup(re.text,'html5lib')

	hdings1=su.findAll("div",{"class":"50_1x_StoryCard mobile-padding"})
	ls=[]
	cont={}
	
	for x in hdings1:
		g=x.find("div",{"class":"story-card"})
		ls.append(g)
	g=0
	for x in ls:
		link=x.find('a')
		img=link.find('img')
		li=[]
		li.append(img.get("title"))
		li.append(link.get("href"))
		li.append(img.get("data-src-template"))
		ss=str(g)
		cont[ss]=li
		g=g+1

	return cont
		
