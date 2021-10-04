from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    my_dect = {'insert_me':"Hello I am from fitst_app/index.html !"}
    return render(request,'fitst_app/index.html',context=my_dect)