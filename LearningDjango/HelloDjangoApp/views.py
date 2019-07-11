# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")
def app(request):
    return HttpResponse("Hello, Django the view that I made!")