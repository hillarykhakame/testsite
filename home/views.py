from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Welcome to my Portoforlio')
    #context = {'name':'Harry','course':'Django'}
    return render(request, 'index.html')

def about(request):
    #return HttpResponse('This is my about page')
    return render(request, 'starter.html')

def projects(request):
    #return HttpResponse('This is my projects page')
    return render(request, 'advanced.html')

def contact(request):
    #return HttpResponse('This is my cointact page')
    #context = {'name':'Larry The Programmer', 'conts':'0795670867,khakamehillary5@gmail.com'}
    return render(request, 'contact.html',)

def htest(request):
    #return HttpResponse('This is my projects page')
    return render(request, 'abouttest.html')

