from django import forms
from mainapp.models import Query,Paper,Review
from django.contrib.auth.models import User
from mainapp.models import Researcher, Review

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
        model = Researcher
        fields = ('name','surname','bio','institution',)

class CreateReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Must be unique'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter a description'}))
    class Meta:
        model = Review
        fields = ('name','description')

#form for new advanced query
class CreateAdvancedQuery(forms.ModelForm):
    query = forms.Textarea()
    class Meta:
        model = Query
        fields = ('query_string',)


#form for abstract pool
class AbstractPoolForm(forms.ModelForm):
    selected_abs = forms.MultipleChoiceField(required = True, widget = forms.CheckboxSelectMultiple) #Still need to add the choices
    class Meta:
        model = Paper
        fields = ('abstract', )


#form for document pool
class DocumentPoolForm(forms.ModelForm):
    selected_docs = forms.MultipleChoiceField(required = True, widget = forms.CheckboxSelectMultiple) #Still need to add the choices
    class Meta:
        model = Paper
        fields = ('paper_url','title','authors',)


#form for final pool
class FinalPoolForm(forms.ModelForm):

    class Meta:
        modal = Paper
