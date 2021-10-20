import requests
import json
from bs4 import BeautifulSoup

checkin="samsung+m12"
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
flipkart=requests.get("https://www.flipkart.com/search?q="+checkin,headers=HEADERS)
amazon=requests.get("https://www.amazon.in/s?k=samsung+m12&ref=nb_sb_noss_2",headers=HEADERS)


fsu=BeautifulSoup(flipkart.text,'html5lib')
asu=BeautifulSoup(amazon.content,'html5lib')


fhead=fsu.findAll("div",{"class":"_4rR01T"},limit=6)
fprice=fsu.findAll("div",{"class":"_30jeq3 _1_WHN1"},limit=6)
fdesc=fsu.findAll("ul",{"class":"_1xgFaf"},limit=6)
frating=fsu.findAll("div",{"class":"_3LWZlK"},limit=6)


adesc=asu.findAll("span",{"class":"a-size-medium a-color-base a-text-normal"},limit=6)
aprice=asu.findAll("div",{"class":"a-row a-size-base a-color-base"},limit=6)
arating=asu.findAll("span",{"class":"a-icon-alt"},limit=6)
g=0



for x in aprice:
	price=x.find('span',{"class":"a-offscreen"})
	print(adesc[g].text)
	print(price.text)
	print(arating[g].text)
	g+=1


print(100*'---')
for x in range(6):
	print(fhead[x].text+"\n")
	print(fprice[x].text+"\n")
	print(fdesc[x].text+"\n")
	print(frating[x].text+"\n")
	



