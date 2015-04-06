from django.shortcuts import render
from .models import Category, Page
from .forms import CategoryForm, PageForm


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


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print form.errors

    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, cat_slug):

    try:
        cat = Category.objects.get(slug=cat_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.save()
                return category(request, cat_slug)

        else:
            print form.errors

    else:
        form = PageForm()

    return render(request, 'rango/add_page.html', {'form': form, 'cat': cat})