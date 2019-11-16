

# Create your models here.
from django.db import models


# current leaves
class Leave(models.Model):
	user = models.CharField(max_length=6)
	leave_type = models.CharField(max_length=30)
	preivous_balance = models.IntegerField()
	total = models.IntegerField()
	used = models.IntegerField()
	balance = models.IntegerField()

data = {
	'Sick Leave' : [0, 8, 0, 8],
	'Earned Leave' : [5, 20, 0, 25],
	'Paternity Leave' : [0,0,0,0],
	'Loss of Pay' : [0,0,0,0],
	'Relocation Leave': [0,0,0,0],
}

LEAVES = [(i, i) for i in data]

class AppliedLeaves(models.Model):
	user = models.CharField(max_length=6)
	start_date = models.DateField()
	end_date = models.DateField()
	leave_type = models.CharField(max_length=30, choices=LEAVES)
	days = models.IntegerField()
	remark = models.CharField(max_length=30)
	approver = models.CharField(max_length=30)
	status = models.CharField(max_length=30, choices=(('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')))

# AppliedLeaves.objects.filter(approver=request.user)
