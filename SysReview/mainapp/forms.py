from django import forms
from mainapp.models import Query,Document,Review
from django.contrib.auth.models import User
from mainapp.models import UserProfile, Review

# Form for new users to register
class UserRegisterForm(forms.ModelForm):

    # Overrides the meta to hide the password properly
    password = forms.CharField(widget=forms.PasswordInput())

    # Adds fields for the username, email and password
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

    # Override the meta to allow passing attributes to the field
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))
    # Overrides the metato allow use of a different,more suitable, widget
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Edit me to save this field'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Edit me to save this field'}))

    # Adds fields for the name, surname, bio and institution
    class Meta:
        model = UserProfile
        fields = ('name','surname','bio','institution',)

class CreateReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Must be unique'}))
    class Meta:
        model = Review
        fields = ('name',)