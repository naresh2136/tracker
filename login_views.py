
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from login.forms import *
from login.models import *

# Create your views here.
def login(request):
    return render(request, "login/login.html")

# Function to add profile
@login_required(login_url="/auth/login/")
def update_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile_info = form.save(commit=False)
            profile_info.user = str(request.user)
            profile_info.save()
            return redirect("/home/")
    return render(request, "login/profile.html", {'form': form})

# Function to show profile
@login_required(login_url="/auth/login/")
def show_profile(request):
    profile_info = Profile.objects.get(user=str(request.user))
    name = profile_info.name
    profile = profile_info.profile.url
    return render(request, "login/show_profile.html", {'profile_info': profile_info, 'name': name, 'profile': profile})


# search users based on user id, name or manager
@login_required(login_url="/auth/login/")
def search_profile(request):
    form = SearchForm()
    if 'user' in request.GET or 'name' in request.GET or 'manager' in request.GET:
        users = []

        if request.GET.get('user'):
            profile_info = Profile.objects.filter(user=str(request.GET.get('user')))
            users.extend(profile_info)

        if request.GET.get('name'):
            profile_info = Profile.objects.filter(name__contains=str(request.GET.get('name')))
            users.extend(profile_info)

        if request.GET.get('manager'):
            profile_info = Profile.objects.filter(manager__contains=str(request.GET.get('manager')))
            users.extend(profile_info)

        return render(request, "login/show.html", {'users': users})
    return render(request, "login/search.html", {'form': form})


# show details of employee
def show_employee(request, id):
    user = Profile.objects.get(user=str(id))
    return render(request, "login/show_employee.html", {'user': user})


def send(request):
    subject = 'Test Django Email'
    message = 'testing'
    email_from = 'test@gmail.com'
    receipient = 'pythontraining.blr@gmail.com'

    send_mail(subject, message, email_from, receipient)
    return redirect("/home/")