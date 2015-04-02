from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'I am a bold font from context.'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'about_message': 'Hi, I am Rango and I am here to serve you.'}
    return render(request, 'rango/about.html', context_dict)
