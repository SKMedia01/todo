from django.shortcuts import render

def homepage(request):
    return HttpResponse("Hello world!")

def secong(request):
    return HttpResponse("Test 2 page")