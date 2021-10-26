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
from cagg.scrapework.toi_business import *

def history(request):
	if request.method == "POST":
		val=request.POST.get('intext')
		return render(request,'history.html',{"content":historyy(val)})
	return render(request,'history.html',{"content":" "})

def index(request):
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
	nbb=int(bb/4)
	return render(request,'index.html',{"content":sports(),"n":range(nll),"nn":range(0,4),"dc":dcnews(),"ndc":range(dcl),"hin":hindu(),"nhi":range(hll),"buis":business(),"nbb":range(nbb)})

