"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import news
from news import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/?$', news.views.news_list, name='news-list'),
    url(r'^/?$', news.views.category_list, name='category-list'),
    url(r'^news/(?P<slug>[\w\-_]+)/$', views.news_detail, name='news_detail'),
    url(r'^category/(?P<slug>[\w\-_]+)/(?P<page>[0-9]+)/$', news.views.category_news_list, name='category-news-list'),
    url(r'^category/(?P<slug>[\w\-_]+)/$', news.views.category_news_list, name='category-news-list'),

]
