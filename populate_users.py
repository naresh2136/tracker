import os
from random import *
from faker import Faker
from random import randrange, randint

f = Faker()

os.environ['DJANGO_SETTINGS_MODULE'] = 'tracker.settings'
import django
django.setup()

from django.contrib.auth.models import User

for i in range(5000, 5010):
    out = 'resu' + '@211'
    user = User.objects.create_user(username=str(i), email='user' + str(i) + '@gmail.com', password=out)


