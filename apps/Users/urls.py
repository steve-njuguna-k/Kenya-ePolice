import imp
from django.urls import path
from apps.Users import views

urlpatterns = [
    path('register/get-started', views.GetStartedRegister, name="GetStartedRegister"),
    path('login/get-started', views.GetStartedLogin, name="GetStartedLogin"),
    path('ocs/register', views.OCSRegister, name="OCSRegister"),
    path('officer/register', views.OfficerRegister, name="OfficerRegister")
]
