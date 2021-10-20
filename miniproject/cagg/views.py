from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
import requests
import json
import math
from bs4 import BeautifulSoup
from cagg.scrapework.toi_sports import *
from cagg.scrapework.history import *



def history(request):
	if request.method == "POST":
		val=request.POST.get('intext')
		return render(request,'history.html',{"content":historyy(val)})
	return render(request,'history.html',{"content":" "})

def index(request):
	ll=int(len(sports()))
	ll=ll-4
	nll=int(ll/4)
	return render(request,'index.html',{"content":sports(),"n":range(nll),"maxx":nll*4})

