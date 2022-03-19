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
from lib.get_data import get_data
from lib.datapiepline import datapiepliner

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from . import models

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "datapiepline.html", context = {
        "files": documents
    })

def main(request):
	return render(request,'index.html')


def exportPdfWeather(request):
    dataDictList = get_data()
    print(dataDictList)
    return render(request,'cooling.html',dataDictList)

def datapiepline(request):
    dataDictList = datapiepliner()
    print(dataDictList)
    return render(request,'datapiepline.html',dataDictList)




def POST_crawl(request):

	#if 'title' in request.GET and request.GET['title']:
	#keywords = input('請輸入工作職缺關鍵字:')
	keywords = request.POST["title"]
	
	url = "https://www.104.com.tw/jobs/search/?keyword=" + keywords +"&jobsource=2018indexpoc&ro=0&order=1"

	options = Options()
	#關閉瀏覽器跳出訊息
	prefs = {
	    'profile.default_content_setting_values' :
	        {
	        'notifications' : 2
	         }
	}
	options.add_experimental_option('prefs',prefs)
	options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
	options.add_argument("--incognito")           #開啟無痕模式

	driver = webdriver.Chrome(ChromeDriverManager().install())

    
	#第一頁內容
	driver.get(url)
     
	with open('result.txt', 'w',encoding='utf-8') as f:
		try:
			for i in range(1,25):

				print('這是第'+ str(i) +'個工作')
				job_company = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[1]/li[2]/a' %(i)).text
				print('公司名稱:' + job_company)
				job_title = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/h2/a' %(i)).text
				print('職缺名稱:' + job_title)
				job_content = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/p' %(i)).text
				print('工作內容:' + job_content)
				job_requirements = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[2]' %(i)).text
				print('工作地點與學經歷:' + '\n' + job_requirements)
				job_salary = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/div/span[1]' %(i)).text
				print('薪水:' + job_salary)
				print('\n')
				target = '這是第'+ str(i) +'個工作' + '\n' + '公司名稱:' + '公司名稱:' + job_company +'\n' + '職缺名稱:' + job_title +'\n' + '工作內容:' + job_content + '\n' + '工作地點與學經歷:' + '\n' + job_requirements + '\n' + '薪水:' + job_salary + '\n\n'
				f.write(target)
		except:
			pass
		driver.close()
	text = []
	with open ('result.txt','r',encoding='utf-8') as f:
		for line in f:
			text.append(line)
	

	return render(request,'result.html',locals()) # render的最後面是返回一個dict,locals()函數會將這個def中的list包成一個dict反值,這邊唯一的list就是text


