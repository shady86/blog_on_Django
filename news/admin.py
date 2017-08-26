# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)