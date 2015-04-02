from django.contrib import admin
from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes')


class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url']
    list_display = ('category', 'title', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)