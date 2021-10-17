from django import forms
from django.forms import fields
from App_Two.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'