import requests
import json
from bs4 import BeautifulSoup

req=str(input("enter here"))
re=requests.get("https://en.wikipedia.org/wiki/"+req)
su=BeautifulSoup(re.text,'html5lib')

hdings1=su.findAll("div",{"class":"mw-body-content mw-content-ltr"})
para=hdings1[0].find("div",{"class":"mw-parser-output"})
p=para.findAll('p')
s=""
for x in p:
	s+=x.text

print(s)
	
