
import os
from random import *
from faker import Faker
from random import randrange, randint

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
            ('1020'),
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

Qual = (('BE'), ('ME'), ('MTech'), ('CA'),('MA'))

years = [1984, 1985, 1989, 1983, 1982]

for i in range(5000, 5010):
    out = 'resu' + '@211'
    #user = User.objects.create_user(username=str(i), email=str(i) + '@gmail.com', password=out)
    uid = str(i)
    name = f.name()
    profile= ""
    mobile = "9845" + str(randrange(100000, 999999))
    manager = managers[randint(0,4)]
    if str(i) in managers:
        manager = str(i)
    primary = PS[randint(0,4)]
    designation = designations[randint(0,4)]
    qual = Qual[randint(0,4)]
    dob =  str(years[randint(0,4)]) + "-0" + str(randrange(1,9))+ "-" + str(randint(10,28))
    doj =  str(randint(2013,2018)) + "-0" + str(randrange(1,9))+ "-" + str(randint(10,28))

    Profile.objects.create(user=str(i), name=name, profile=profile, mobile=mobile, manager=manager, primary_skill=primary, designation=designation, doj=doj, dob=dob, qual=qual)

"""
class Profile (models.Model):
    user = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    profile = models.ImageField(upload_to="images/")
    mobile = models.IntegerField()
    manager = models.CharField(max_length=30, choices=managers)
    primary_skill = models.CharField(max_length=30, choices=PS)
    designation = models.CharField(max_length=30, choices=designations)
    doj = models.DateField()
    dob = models.DateField()
    qual = models.CharField(max_length=30, choices=Qual)
"""