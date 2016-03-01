from django import forms
from mainapp.models import Query,Document,Review
from django.contrib.auth.models import User


# Form for users to log in
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


# Form for new users to register
class UserRegisterForm(forms.ModelForm):
    #Overrides the meta to hide the password properly
    password = forms.CharField(widget=forms.PasswordInput())

    #Adds fields for the username, email and password
    class Meta:
        model = User
        fields = ('username','email','password')