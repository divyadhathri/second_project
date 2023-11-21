from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhatri(request):
    return HttpResponse('<marquee><h1>i am divyadhatri</h1></marquee>')