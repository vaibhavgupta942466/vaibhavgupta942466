from django.conf.urls import url
from fitst_app import views

urlpatterns = [
    url('^$',views.index,name='index'),
]
