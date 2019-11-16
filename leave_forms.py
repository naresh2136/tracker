# Create your views here.
from django import forms
from leave.models import *
import re
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class ApplyLeaveForm(forms.ModelForm):
	class Meta:
		model = AppliedLeaves
		fields = ['start_date', 'end_date', 'leave_type', 'remark']
		widgets = {
			'start_date': DatePickerInput(format="%d/%m/%Y"),
			'end_date': DatePickerInput(format="%d/%m/%Y"),
		}
