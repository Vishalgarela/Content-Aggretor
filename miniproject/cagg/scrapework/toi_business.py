import requests
import json
from bs4 import BeautifulSoup

def business():
	re=requests.get("https://www.business-standard.com/")
	su=BeautifulSoup(re.content,'html5lib')

	stories=su.findAll("div",{"class","btm-section"})
	article=stories[0].findAll("div",{"class":"article"})
	
	cont={}
	g=0
	for x in article:
		link=x.find("a")
		im=link.find("img")
		title=x.find("h2")
		
		li=[]
		li.append(title.text.strip())
		li.append("https://www.business-standard.com/"+link.get("href"))
		li.append(im.get("src"))
		ss=str(g)
		cont[ss]=li
		g+=1
	
	return cont


