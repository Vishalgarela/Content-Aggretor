from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
import requests
import json
from bs4 import BeautifulSoup
from cagg.scrapework.toi_sports import *
from cagg.scrapework.history import *



def summaryy(request):
	if request.method == "POST":
		val=request.POST.get('intext')
	return render(request,'summary.html',{"content":historyy(val)})

def history(request):
	return render(request,'history.html')

def index(request):

	return render(request,'index.html',{"content":sports(),"n":range(4)})

