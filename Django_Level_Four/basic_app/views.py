from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'html/index.html')

def other(request):
    return render(request,'html/other.html')

def relative(request):
    return render(request,'html/relative_url_templates.html')
