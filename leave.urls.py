from django.urls import path, include
from leave.views import *


urlpatterns = [
    path('apply_leave/', apply_leave),
    path('approve_leave/', approve_leave),
]
