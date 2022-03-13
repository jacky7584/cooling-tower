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
from first.views import sayhello,hello2,hello3,hello4,main,POST_crawl,listone,listall,insert,modify,delete,exportPdfWeather,datapiepline
urlpatterns = [
    path('admin/', admin.site.urls),
    #hello世界範例1
    #url(r'^$', sayhello),
    #url(r'^hello2/(\w+)/$', hello2),
    #url(r'^hello3/(\w+)/$', hello3),
    #url(r'^hello4/(\w+)/$', hello4),
    
    #爬蟲範例1
    path('',main),                 #在首頁下執行main函式
    path('POST_crawl/',POST_crawl), #在POST_crawl頁面執行POST_crawl函式

    #database測試
    url(r'^listone/$', listone),
    url(r'^listall/$', listall),
    url(r'^insert/$', insert),   #新增資料
    url(r'^modify/$', modify),   #修改資料
    url(r'^delete/$', delete),   #刪除資料

    #冰水主機首頁
    path('api/exportPdfWeather/', exportPdfWeather),
    #冰水主機分群分析
    path('api/datapiepline/', datapiepline),
]
