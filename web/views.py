from django.shortcuts import render
from django.http.response import HttpResponse, StreamingHttpResponse
import datetime


def getdatetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    return render(request, 'index.html')