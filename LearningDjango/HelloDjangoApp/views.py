# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def index(request):
    now = datetime.now()

    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X"),
            
        }
    )
def app(request):
    a=5
    return render(
        request,
        "HelloDjangoApp/app.html",
        {
            'ColumnName': "Total Impressions",
            'value':a
        }
    )