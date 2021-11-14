from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
import requests
import json
from bs4 import BeautifulSoup
from cagg.scrapework.toi_sports import *
from cagg.scrapework.history import *
from cagg.scrapework.toi_business import *
from cagg.scrapework.dc_scrape import *
from cagg.scrapework.hindu_scrape import *
from cagg.scrapework.seo import *
from cagg.scrapework.ndtv import *
from cagg.scrapework.tech import *

from rake_nltk import Rake

import nltk
import requests
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def price(request):
	if request.method == "POST":
		val=request.POST.get('intext')
		result=seokeywords(val)
		stop_words = set(stopwords.words("english"))
		words = word_tokenize(result)
		stem = PorterStemmer()
		frequency_table = dict()
		for wd in words:
			wd = stem.stem(wd)
			if wd in stop_words:
				continue
			if wd in frequency_table:
				frequency_table[wd] += 1
			else:
				frequency_table[wd] = 1
		lis=list(frequency_table.values())
		summ=0
		for x in lis:
			summ+=int(x)

		try:
			del frequency_table[',']
			del frequency_table['.']
			del frequency_table['(']
			del frequency_table[')']
			del frequency_table[';']
			del frequency_table['|']
			del frequency_table['&']
			del frequency_table['%']
			del frequency_table['!']
		except Exception as err:
			pass	

		cont={}

		r=Rake()
		r.extract_keywords_from_text(result)
		hh=r.get_ranked_phrases()[0:10]
		phr={}
		phr['0']=hh

		for x in range(10):
			Keymax = max(frequency_table, key= lambda x: frequency_table[x])
			li=[]
			li.append(Keymax)
			cnt=int(frequency_table.get(Keymax))
			li.append((cnt/summ*100))
			cont[str(x)]=li
			del frequency_table[Keymax]

		return render(request,'price.html',{"count":cont,"n":range(10),"phr":phr})
	
	return render(request,'price.html')
def history(request):
	if request.method == "POST":
		val=request.POST.get('intext')
		return render(request,'summary.html',{"content":historyy(val)})
	return render(request,'history.html',{"content":" "})

def index(request):
	techlen=int(len(tech()))
	techlen=techlen-4
	techll=int(techlen/4)
	ndtvlen=int(len(ndtv()))
	ndtvlen=ndtvlen-4
	nddll=int(ndtvlen/4)
	ll=int(len(sports()))
	ll=ll-4
	nll=int(ll/4)
	dc=int(len(dcnews()))
	dc=dc-4
	dcl=int(dc/4)
	hh=int(len(hindu()))
	hh=hh-4
	hll=int(hh/4)
	bb=int(len(business()))
	bb=bb-4
	nbuis=int(bb/4)
	return render(request,'index.html',{"content":sports(),"n":range(nll),"nn":range(0,4),"dc":dcnews(),"ndc":range(dcl),"hin":hindu(),"nhi":range(hll),"buis":business(),"nbb":range(nbuis),"ndtv":ndtv(),"ndtvrange":range(nddll),"tech":tech(),"ntech":range(techll)})

