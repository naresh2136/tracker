from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from holidays.models import *
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url="/auth/login/")
def holidays(request):
    current_year = datetime.datetime.now().year
    holidays = Holidays.objects.filter(year=current_year)
    return render(request, r'holidays/holidays.html', {'holidays' : holidays})

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['pythontraining.blr@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('redirect to a new page')
