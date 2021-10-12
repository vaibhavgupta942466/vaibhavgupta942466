from django.shortcuts import render
from django.http import HttpResponse
from fitst_app.models import Topic,Webpage,AccessRecord


# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':Webpages_list}
    # my_dict = {'insert_me':"Hello I am from fitst_app/index.html !"}
    return render(request,'fitst_app/index.html',context=date_dict)