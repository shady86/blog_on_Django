# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from news.models import *
from django.views import generic
from news import models

# Create your views here.

def index(request):

    news = News.objects.all()
    context = {'zmienna': 'widok',
                'news': news}
    return render(request, 'index.html', context)


class NewsList(generic.ListView):
    model = models.News
    paginate_by = 10
    context_object_name = 'news_list'

news_list = NewsList.as_view()

class CategoryList(generic.ListView):
    model = models.Category
    context_object_name = 'category_list'

category_list = CategoryList.as_view()

class NewsDetailView(generic.DetailView):
    model = models.News

news_detail = NewsDetailView.as_view()


class CategoryNewsList(NewsList):
    template_name = 'news/category_news_list.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryNewsList, self).get_context_data(**kwargs)
        context['category'] = self._get_category()
        return context

    def get_queryset(self):
        category = self._get_category()
        return models.News.objects.filter(categories=category)

    def _get_category(self):
        return models.Category.objects.get(slug=self.kwargs['slug'])

category_news_list = CategoryNewsList.as_view()


