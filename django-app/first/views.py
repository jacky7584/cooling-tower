from datetime import datetime
from pkgutil import get_data

from django.http import HttpResponse
from django.shortcuts import render


def sayhello(request):
   return HttpResponse("Hello django!")
def hello2(reuest,username):
   return HttpResponse("Hello" + username)
def hello3(request,username):
   now=datetime.now()
   return render(request,"hello3.html",locals())

def hello4(request,username):
   now=datetime.now()
   return render(request,"hello4.html",locals())
# Create your views here.


import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lib.get_data import get_data,get_list
from lib.datapiepline import datapiepliner
import time # 引入time
from datetime import datetime



from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from . import models
from .models import field
from django.http import JsonResponse 
def test(request):
    dataDictList = get_data()
    a = field.objects.all()
    print(dataDictList)
    dataDictList['aa']=a
    return render(request,'dashbord.html',dataDictList)

def test1(request):
    dataDictList = get_data()
    a = field.objects.all()
	#how to get database data
    #dataDictList['aa']=a
    print(dataDictList)
    result = {'State': 'Successful'}
    return JsonResponse(dataDictList) 


def main(request):
	return render(request,'index.html')


def exportPdfWeather(request):
    dataDictList = get_data()
    a = field.objects.all()
    print(a)
    dataDictList['aa']=a
    return render(request,'cooling.html',dataDictList)

def dataAnalytics(request):
	 return render(request,'dataAnalytics.html')


def showplt(request ):
	if request.method == "POST":
		point=request.POST['point']
		picker_start=request.POST['picker_start']
		picker_end=request.POST['picker_end']
		dataplt=datapiepliner(point,picker_start,picker_end)
		day=[]
		first=int(time.mktime( time.strptime(picker_start, "%Y-%m-%d")))
		end=int(time.mktime( time.strptime(picker_end, "%Y-%m-%d")))
		for i in range(first,end,86400):
			realday=datetime.fromtimestamp(i).strftime('%Y-%m-%d') 
			day.append(realday)
		dataplt['day']=day
		return render(request,'datapiepline.html',dataplt)
	else:
		return render(request,'datapiepline.html')







