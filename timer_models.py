
from django.db import models

# Create your models here.
class TimeSheetData(models.Model):
    user = models.CharField(max_length=30)
    project = models.CharField(max_length=30)
    approver = models.CharField(max_length=30, null=True, blank=True)
    hours = models.IntegerField()
    date = models.DateField()
    desc = models.CharField(max_length=50)
    status = models.CharField(max_length=30, default='Pending')