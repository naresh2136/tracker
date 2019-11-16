
from django import forms
from login.models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class SearchForm(forms.Form):
    user = forms.CharField(max_length=30, required=False)
    name = forms.CharField(max_length=30, required=False)
    manager = forms.CharField(max_length=30, required=False)
