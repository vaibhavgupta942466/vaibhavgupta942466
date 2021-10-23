from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        Model = User
        fields = ('username','email','password')