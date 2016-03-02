from django import forms
from mainapp.models import Query,Document,Review
from django.contrib.auth.models import User
from mainapp.models import UserProfile

# Form for new users to register
class UserRegisterForm(forms.ModelForm):

    #Overrides the meta to hide the password properly
    password = forms.CharField(widget=forms.PasswordInput())

    #Adds fields for the username, email and password
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Edit me to save this field'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))
    class Meta:
        model = UserProfile
        fields = ('name','surname','bio','institution',)