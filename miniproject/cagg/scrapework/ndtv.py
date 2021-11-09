import requests
import json
from bs4 import BeautifulSoup

def ndtv():
	re=requests.get("https://www.ndtv.com/")
	ndd=BeautifulSoup(re.text,'html5lib')

	topstories=ndd.findAll("div",{"class":"featured_cont"})
	ull=topstories[0].find("ul")
	g=0
	cont={}
	for x in ull:

		try:
			li=[]
			cc=x.find("a")
			im=cc.find("img")
			li.append(im.get("alt"))
			li.append(cc.get("href"))
			li.append(im.get("src"))
			ss=str(g)
			cont[ss]=li
			g+=1

		except Exception as err:
			pass

	return cont

