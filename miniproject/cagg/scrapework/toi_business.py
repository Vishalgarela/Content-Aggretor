import requests
import json
from bs4 import BeautifulSoup

def business():
	re=requests.get("https://timesofindia.indiatimes.com/business")
	su=BeautifulSoup(re.text,'html5lib')

	hdings1=su.findAll("div",{"class":"top-newslist small"})
	hdings1.pop(1)
	

	ul=hdings1[0].find('ul')
	

	lis1=[]
	
	for x in ul:
		lis1.append(x)

	

	cont={}
	cnt=0
	for x in lis1:
		try:
			span=x.find('span')  #no images given in website 
			link=span.find('a')
			ss=str(cnt)
			lii=[]
			lii.append(link.get('title'))
			lii.append(link.get('href'))
			
			cont[ss]=lii
			cnt+=1 

		except Exception as e:
			continue
	return cont


