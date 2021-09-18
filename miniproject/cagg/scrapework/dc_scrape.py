import requests
import json
from bs4 import BeautifulSoup

re=requests.get("https://www.deccanchronicle.com/")
su=BeautifulSoup(re.text,'html5lib')

hdings1=su.findAll("div",{"class":"col-sm-3 col-xs-12 tstry-feed-sml-a"})
hdings2=su.findAll("div",{"class":"col-sm-12 col-xs-12 tstry-feed-sml-a"})

lis1=[]
lis2=[]
for x in hdings1:
	lis1.append(x)
for x in hdings2:
	lis2.append(x)



further1=[]
further2=[]
for x in lis1:
	further1.append(x.find("a"))

for x in lis2:
	further2.append(x.find("a"))

#data of top stories
for x in further2:
	print("link: "+x.get("href")+'\n') #this link is to be concatinated by home link
	tt=x.find("h3")
	print(tt.text+'\n')
	im=x.find("img")
	print(im.get("data-src")+'\n')
	print(im.get("title")+'\n')
	print('**'*50)

for x in further1:
	tt=x.find("h3")
	print(tt.text+'\n')
	im=x.find("img")
	print(im.get("data-src")+'\n')
	print(im.get("title")+'\n')
	print('**'*50)





	



# for x in li:
# 	im=x.find("img")
# 	print(im)
	# print(im.get("data-src"))
	# print(im.get("title"))


# with open('data.txt', 'w') as outfile:
# 	json.dump(ans,outfile)


#for x in hd2:
#	print(x)