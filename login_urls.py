
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from login.views import *

urlpatterns = [
    path('login/', login),
    path('get_logged_in/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', update_profile),
    path('show_profile/', show_profile),
    path('search_profile/', search_profile),
    path('employee/<int:id>/', show_employee),
    path('send/', send),
]