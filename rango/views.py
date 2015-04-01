from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Rango says hey there world!\nGo to the <a href="about/">about</a> page.')


def about(request):
    return HttpResponse('Rango says here is the about page.\nGo back to the <a href="/rango/">main</a> page.')
