from django.shortcuts import render

from django.http import HttpResponse



def home(request):
    return HttpResponse('This is home and it is my first home page')

def page1(request):
    return HttpResponse('This is my first page ')

def page2(request):
    return  HttpResponse('This is my second page  ')
