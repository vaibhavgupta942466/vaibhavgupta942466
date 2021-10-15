from django.conf.urls import url
from App_Two import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
