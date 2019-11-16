
from django.db import models

# Create your models here.



# Create your models here.
class Holidays(models.Model):
	year = models.IntegerField()
	date = models.DateField()
	day = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)