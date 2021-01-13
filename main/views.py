from django.shortcuts import render

def homepage(request):
    return HttpResponse("Hello world!")

def second(request):
    return HttpResponse("Test 2 page")

def third(request):
    return HttpResponse("Test 3 page") 
