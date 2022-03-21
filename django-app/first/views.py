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

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from . import models

def uploadFile(request):

    if request.method == "POST":
        # Fetching the form data
      
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(

            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()
	
    return render(request, "datapiepline.html", context = {
        "files": documents
    })

def featurelist(request):
    dataDictList = get_list()
    print(dataDictList)
    return render(request,'datapiepline.html',dataDictList)


def main(request):
	return render(request,'index.html')


def exportPdfWeather(request):
    dataDictList = get_data()
    print(dataDictList)
    return render(request,'cooling.html',dataDictList)







