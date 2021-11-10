import requests
import json
from bs4 import BeautifulSoup




def tech():
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})
	tech=requests.get("https://gadgets.ndtv.com/news",headers=HEADERS)
	technews=BeautifulSoup(tech.content,'html5lib')
	hdings=technews.findAll("div",{"class","story_list row margin_b30"})
	li=[]
	for x in hdings:
		try:
			li.append(x.find("ul"))
		except Exception as error:
			pass
	cl=li[0].findAll("div",{"class":"thumb"})
	cont={}
	g=0
	for x in cl:
		lis=[]
		link=x.find("a")
		im=link.find('img')
		lis.append(im.get("title"))
		lis.append(link.get("href"))
		if(im.get("data-original")==None):
			lis.append(im.get("src"))
		else:
			lis.append(im.get("data-original"))

		ss=str(g)
		cont[ss]=lis
		g+=1

	return cont

tech()