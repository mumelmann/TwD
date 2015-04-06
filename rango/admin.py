from django.contrib import admin
from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url', 'views']
    list_display = ('category', 'title', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)