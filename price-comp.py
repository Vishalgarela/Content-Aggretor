import requests
import json
from bs4 import BeautifulSoup
checkin="iphone12"
flipkart=requests.get("https://www.flipkart.com/search?q="+checkin)
amazon=requests.get("https://www.amazon.in/s?k="+checkin)
fsu=BeautifulSoup(flipkart.text,'html5lib')
asu=BeautifulSoup(amazon.text,'html5lib')

fhead=fsu.findAll("div",{"class":"_4rR01T"},limit=6)
fprice=fsu.findAll("div",{"class":"_30jeq3 _1_WHN1"},limit=6)
fdesc=fsu.findAll("ul",{"class":"_1xgFaf"},limit=6)
for x in range(6):
	print(fhead[x].text+"\n")
	print(fprice[x].text+"\n")
	print(fdesc[x].text+"\n")
	print(100*"--")



