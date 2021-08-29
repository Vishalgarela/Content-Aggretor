from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
import requests
import json
from bs4 import BeautifulSoup


def index(request):
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
	cont={}
	cn=0
	for x in li:
	 	link=x.find("a")
	 	im=link.find("img")
	 	inner=[]  
	 	inner.append(x.text)
	 	inner.append(link.get("href"))
	 	inner.append(im.get("data-src"))
	 	ss="ho"+str(cn)
	 	cont[ss]=inner
	 	cn+=1
	


	return render(request,'index.html',{"content":cont})

