import os
from random import *
from faker import Faker

os.environ['DJANGO_SETTINGS_MODULE'] = 'tracker.settings'

import django

django.setup()

from leave.models import *

f1 = Faker()

data = {
    'Sick Leave': [0, 8, 0, 8],
    'Earned Leave': [5, 20, 0, 25],
    'Paternity Leave': [0, 0, 0, 0],
    'Loss of Pay': [0, 0, 0, 0],
    'Relocation Leave': [0, 0, 0, 0],
}


def populate(x, y):
    for i in range(x, y + 1):
        user = str(i)
        for leave_type in data:
            preivous_balance = data[leave_type][0]
            total = data[leave_type][1]
            used = data[leave_type][2]
            balance = data[leave_type][3]
            Leave.objects.get_or_create(user=user, leave_type=leave_type, preivous_balance=preivous_balance,
                                        total=total, used=used, balance=balance)


populate(5000, 5000)