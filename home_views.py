from django.shortcuts import render

# Create your views here.
from login.models import *

# Create your views here.
def home(request):

    return render(request, "home/home.html")
