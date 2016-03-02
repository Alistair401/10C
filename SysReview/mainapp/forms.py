from django import forms
from mainapp.models import Query,Document,Review
from django.contrib.auth.models import User


# Form for users to log in
class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['username','password']





# Form for new users to register
class UserRegisterForm(forms.ModelForm):
    #Overrides the meta to hide the password properly
    password = forms.CharField(widget=forms.PasswordInput())

    #Adds fields for the username, email and password
    class Meta:
        model = User
        fields = ('username','email','password')