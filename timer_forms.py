
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
        }

class SelectDateForm(forms.Form):
    start_date = forms.DateField(widget=DatePickerInput(), label='Start Date')
    end_date = forms.DateField(widget=DatePickerInput(), label='End Date')
    labels = {
        'start_date': 'Start Date',
        'end_date': 'End Date',
    }