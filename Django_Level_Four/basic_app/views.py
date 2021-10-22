from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'html/index.html',context_dict)

def other(request):
    return render(request,'html/other.html')

def relative(request):
    return render(request,'html/relative_url_templates.html')
