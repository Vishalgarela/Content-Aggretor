import requests
import json
from bs4 import BeautifulSoup




def seokeywords(checkin):

	
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})
	seo=requests.get(checkin,headers=HEADERS)

	seokey=BeautifulSoup(seo.content,'html5lib')

	result=""
	para=seokey.findAll('p')
	link=seokey.findAll('a')
	head=seokey.findAll('h1')
	head2=seokey.findAll('h2')
	for x in head2:
		result+=" "+x.text
	for x in link:
		result+=" "+x.text
	for x in para:
		result+=" "+x.text

	return result



	# fhead=fsu.findAll("div",{"class":"_4rR01T"},limit=6)
	# fimg=fsu.findAll("img",{"class":"_396cs4 _3exPp9"},limit=6)
	# fprice=fsu.findAll("div",{"class":"_30jeq3 _1_WHN1"},limit=6)
	# fdesc=fsu.findAll("ul",{"class":"_1xgFaf"},limit=6)
	# frating=fsu.findAll("div",{"class":"_3LWZlK"},limit=6)
	# flink=fsu.findAll("a",{"class":"_1fQZEK"},limit=6)

	


	# aimg=asu.findAll("div",{"class":"a-section aok-relative s-image-fixed-height"},limit=6)
	# adesc=asu.findAll("span",{"class":"a-size-medium a-color-base a-text-normal"},limit=6)
	# aprice=asu.findAll("div",{"class":"a-row a-size-base a-color-base"},limit=6)
	# arating=asu.findAll("span",{"class":"a-icon-alt"},limit=6)
	# alink=asu.findAll("a",{"class":"a-link-normal s-no-outline"},limit=6)
	# g=0
	
	# amz={}

	# for x in aprice:
	# 	price=x.find('span',{"class":"a-offscreen"})
	# 	li=[]
	# 	dd=aimg[g].find("img")
	# 	li.append(dd.get("src"))
	# 	li.append(adesc[g].text)
	# 	li.append(price.text)
	# 	li.append(arating[g].text)
	# 	li.append("amazon.in"+alink[g].get("href"))
	# 	ss=str(g)
	# 	amz[g]=li
	# 	g+=1
	# flip={}
	# g=0
	# for x in range(6):
	# 	li=[]
	# 	li.append(fimg[x].get("src"))
	# 	li.append(fhead[x].text)
	# 	li.append(fprice[x].text)
	# 	li.append(fdesc[x].text)
	# 	li.append(frating[x].text)
	# 	li.append("flipkart.com"+flink[x].get("href"))
	# 	ss=str(g)
	# 	flip[g]=li
	# 	g+=1
	# return amz,flip
