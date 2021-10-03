import requests
import json
from bs4 import BeautifulSoup

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

def historyy():
	req+=" wikipedia"
	mainlink=""
	for j in search(req, tld="co.in", num=10, stop=10, pause=2):
		mainlink+=j
		break

	re=requests.get(mainlink)
	su=BeautifulSoup(re.text,'html5lib')

	hdings1=su.findAll("div",{"class":"mw-body-content mw-content-ltr"})
	para=hdings1[0].find("div",{"class":"mw-parser-output"})
	p=para.findAll('p')
	s=""
	for x in p:
		s+=x.text

	cont={"his":s}
	return cont
	
