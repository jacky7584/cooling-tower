"""LINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from first.views import main,exportPdfWeather,uploadFile,featurelist
urlpatterns = [
    path('admin/', admin.site.urls),
    #hello世界範例1
    #url(r'^$', sayhello),
    #url(r'^hello2/(\w+)/$', hello2),
    #url(r'^hello3/(\w+)/$', hello3),
    #url(r'^hello4/(\w+)/$', hello4),
    
    #爬蟲範例1
    path('',main),                 #在首頁下執行main函式


    #冰水主機首頁
    path('api/exportPdfWeather/', exportPdfWeather),
    #資料上傳處理
    path("api/uploadFile/", uploadFile, name = "uploadFile"),
    path("api/uploadFile/", featurelist),
]
