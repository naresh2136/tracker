
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
managers = (
            ('1000','1000'),
            ('1010','1010'),
            ('1020','1020'),
            ('1020','1020'),
            ('1030','1030'),
)

designations = (
            ('Trainee Engineer', 'Trainee Engineer'),
            ('Software Engineer', 'Software Engineer'),
            ('Lead Engineer', 'Lead Engineer'),
            ('Analyst','Analyst'),
            ('Admin','Admin'),
)

PS = (
    ('Python', 'Python'),
    ('C#', 'C#'),
    ('Perl', 'Perl'),
    ('Java', 'Java'),
)

Qual = (('BE', 'BE'), ('ME', 'ME'), ('MTech', 'MTech'))

class Profile (models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    profile = models.ImageField(upload_to="images")
    mobile = models.CharField(max_length=30)
    manager = models.CharField(max_length=30, choices=managers)
    primary_skill = models.CharField(max_length=30, choices=PS)
    designation = models.CharField(max_length=30, choices=designations)
    qual = models.CharField(max_length=30, choices=Qual)
    dob = models.DateField(default=datetime.now())
    doj = models.DateField(default=datetime.now())

'''
class Manager(models.Model):
    manager = models.CharField(max_length=30)
    employee = models.CharField(max_length=30)
'''

"""
Profile.objects.create(user='5001', name='Ajay', profile='images/5000.jpg', mobile='9900332211', manager='1010', primary_skill='Perl', designation='Admin', qual='BE', dob=datetime(1984, 10, 24), doj=(2015, 11, 17)) 
"""