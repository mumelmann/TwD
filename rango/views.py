from django.shortcuts import render
from .models import Category, Page


def index(request):
    cat_list = Category.objects.all()[:5]
    popular_pages = Page.objects.order_by('-views')[:5]
    return render(request, 'rango/index.html', {'cat_list': cat_list, 'popular_pages': popular_pages})


def about(request):
    context_dict = {'about_message': 'Hi, I am Rango and I am here to serve you.'}
    return render(request, 'rango/about.html', context_dict)


def category(request, cat_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=cat_slug)
        pages = Page.objects.filter(category=category)
        context_dict['cat_name'] = category.name
        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)