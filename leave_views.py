from django.shortcuts import render
from django.contrib import messages
from leave.forms import *
from leave.models import *

import calendar
from datetime import timedelta, date, datetime
import re

def find_day(date):
    born = datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


def date_range(start_date, end_date):
    all_dates = []
    for n in range(int((end_date - start_date).days)):
        all_dates.append(start_date + timedelta(n))
    return all_dates


def apply_leave(request):
    form = ApplyLeaveForm()
    if request.method == "POST":
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            leave_type = form.cleaned_data['leave_type']
            remark = form.cleaned_data['remark']
            days = (end - start).days + 1

            print(start, end)

            profile = Profile.objects.get(user=request.user)
            approver = profile.manager

            status = "Pending"

            all_dates = date_range(start, end)

            for d in all_dates:
                #if Holidays.objects.filter(date=d).count() > 0:
                #    days = days - 1
                #    continue
                d = d.strftime('%d %m %Y')
                if re.search("Sat|Sun", find_day(d), flags=re.I):
                    days = days - 1

            print(start, end, days, leave_type, remark)

            AppliedLeaves.objects.create(start_date=start, end_date=end, days=days, leave_type=leave_type,
                                         remark=remark, status=status, approver=approver)
            user = str(request.user)
            leave = Leave.objects.get(user=user, leave_type=leave_type)
            leave.used = leave.used + days
            leave.balance = leave.balance - days
            leave.save()
            messages.info(request, 'Successfully applied leave!!')
    leaves = Leave.objects.filter(user=str(request.user))
    return render(request, r'leave/apply_leave.html', {'leaves': leaves, 'form': form})


def approve_leave(request):
    leaves = AppliedLeaves.objects.filter(approver=str(request.user), status='Pending')
    print(leaves, len(leaves) + 1)
    if request.method == "POST":
        for i in range(1, len(leaves) + 1):
            id = leaves[i - 1].__dict__['id']
            leave = AppliedLeaves.objects.get(id=id)
            status = request.POST.get('status' + str(i))
            leave.status = status
            leave.save()
    return render(request, r'leave/apply_leave.html', {'leaves': leaves})

