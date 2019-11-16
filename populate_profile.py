
import os
from random import *
from faker import Faker
from random import randrange, randint
from datetime import datetime

f = Faker()

os.environ['DJANGO_SETTINGS_MODULE'] = 'tracker.settings'
import django
django.setup()

from login.models import *
from django.contrib.auth.models import User

managers = (
            ('1000'),
            ('1010'),
            ('1020'),
            ('1040'),
            ('1030'),
)

designations = (
            ('Trainee Engineer'),
            ('Software Engineer'),
            ('Lead Engineer'),
            ('Analyst'),
            ('Admin'),
)

PS = (
    'Python',
    'C#',
    'Perl',
    'Java',
    'Scala',
)

Qual = (('BE'), ('ME'), ('MTech'), ('CA'), ('MA'))

years = [1984, 1985, 1989, 1983, 1982]

for i in range(6500, 6510):
    out = 'resu' + '@' + str(i)
    user = User.objects.create_user(username=str(i), email='user' + str(i) + '@gmail.com', password=out)
    uid = str(i)
    name = f.name()
    profile = "images/" + str(i) + ".jpg"
    mobile = "9845" + str(randrange(100000, 999999))
    manager = managers[randint(0,4)]

    primary = PS[randint(0,4)]
    designation = designations[randint(0,4)]
    qual = Qual[randint(0,4)]
    dob = datetime(randrange(1980, 1995), randrange(1,12), randrange(1, 28))
    doj = datetime(randrange(2010, 2018), randrange(1,12), randrange(1, 28))
    Profile.objects.create(user=str(i), name=name, profile=profile, mobile=mobile, manager=manager, primary_skill=primary, designation=designation, doj=doj, dob=dob, qual=qual)
