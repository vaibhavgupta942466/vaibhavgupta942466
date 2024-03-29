from django.shortcuts import render
from django.http import HttpResponse
from App_Two.models import User
from App_Two.forms import NewUserForm
# Create your views here.

# def index(request):
#     return HttpResponse("<em>My Second App</em>")

# def help(request):
#     helpdict  = {'help_insert':''}
#     return render(request,'help.html',context=helpdict)

def index(request):
    return render(request,'index.html')

# def users(request):

#     user_list = User.objects.order_by('First_Name')
#     user_dict = {'users':user_list}
#     return render(request,'users.html',context=user_dict)

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid!')
    return render(request,'users.html',{'form':form})

