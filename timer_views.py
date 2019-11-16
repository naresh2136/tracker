


# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tim.forms import *
from tim.models import *
from leave.models import *
from login.models import *

from django.contrib.auth import login, authenticate
from datetime import timedelta, date, datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')


def after(request):
    print(request.user)
    print(request.user.get_username())
    return HttpResponse("Success")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/after/')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {'form': form})


def select_dates(request):
    form = SelectDateForm()
    if request.method == "POST":
        form = SelectDateForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            print("=>", start, end)
            #date1 = datetime.strptime(start, "%Y-%m-%d").date()
            #date2 = datetime.strptime(end, "%Y-%m-%d").date()
            date1 = start
            date2 = end
            print("TImehseet", date1, date2)
            all_data = []

            # get current user's project name from profile
            profile = Profile.objects.get(user=request.user)
            project = profile.project

            # expand the dates
            for n in range(int((date2 - date1).days) + 1):
                x = date1 + timedelta(n)
                print(x, type(x))
                m = x.strftime("%Y-%m-%d")
                print(m, type(m))
                all_data.append([n+1, project, 'HOURS', x, 'DESC'])

            # show the table form with expanded dates
            # allows user to type timesheet for selected date ranges
            return render(request, "tracker/enter_timesheet.html", {'dates': all_data})

    return render(request, "tracker/select_date.html", {'form': form})

def submit(request):
    timesheet_data = []
    try:
        for i in range(1, 10):
            hours = request.POST.get('hours' +str(i))
            date = request.POST.get('date' +str(i))
            desc = request.POST.get('desc' +str(i))
            if hours != None:
                timesheet_data.append([hours, date, desc])
    except:
        pass

    profile = Profile.objects.get(user=request.user)
    project = profile.project
    approver = profile.manager
    for data in timesheet_data:
        date = data[1].split("-")
        date = [int(i) for i in date]
        TimeSheetData.objects.create(user=request.user, project=project, hours=int(data[0]), date=datetime(date[2], date[1], date[0]), desc=data[-1], status='Pending', approver=approver)

    return redirect("/tim/select_dates/")


def approve_timesheet(request):
    # Get all applied timesheet data where logged-in user is approver
    timesheet = TimeSheetData.objects.filter(approver=str(request.user), status='Pending')

    # change the status while submitting
    if request.method == "POST":
        for i in range(1, len(timesheet) + 1):
            id = timesheet[i - 1].__dict__['id']
            data = TimeSheetData.objects.get(id=id)
            status = request.POST.get('status' + str(i))
            data.status = status
            data.save()
            redirect("/home/")

    return render(request, r'tracker/timesheet.html', {'timesheets': timesheet})
