import requests
import json
from bs4 import BeautifulSoup


def dcnews():
		re=requests.get("https://www.deccanchronicle.com/")
		su=BeautifulSoup(re.text,'html5lib')

		hdings1=su.findAll("div",{"class":"col-sm-3 col-xs-12 tstry-feed-sml-a"})
		hdings2=su.findAll("div",{"class":"col-sm-12 col-xs-12 tstry-feed-sml-a"})

		lis1=[]
		
		for x in hdings2:
			lis1.append(x)
		



		further1=[]
		
		for x in lis1:
			further1.append(x.find("a"))

		

		#data of top stories
		cont={}
		g=0
		for x in further1:
			li=[]
			
			im=x.find("img")
			li.append(im.get("title"))
			li.append("https://www.deccanchronicle.com"+x.get("href"))
			li.append(im.get("data-src"))
			
			ss=str(g)
			cont[ss]=li
			g+=1

		

		return cont




	



# for x in li:
# 	im=x.find("img")
# 	print(im)
	# print(im.get("data-src"))
	# print(im.get("title"))


# with open('data.txt', 'w') as outfile:
# 	json.dump(ans,outfile)


#for x in hd2:
#	print(x)