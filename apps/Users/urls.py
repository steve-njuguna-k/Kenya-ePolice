import imp
from django.urls import path
from apps.Users import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('register/get-started', views.GetStartedRegister, name="GetStartedRegister"),
    path('login/get-started', views.GetStartedLogin, name="GetStartedLogin"),
    path('ocs/register', views.OCSRegister, name="OCSRegister"),
    path('ocs/login', views.OCSLogin, name="OCSLogin"),
    path('officer/register', views.OfficerRegister, name="OfficerRegister"),
    path('officer/login', views.OfficerLogin, name="OfficerLogin"),
    path('activateuser/<uidb64>/<token>',views.ActivateAccount, name = 'ActivateAccount'),
    path('officer/dashboard', views.OfficerDashboard, name="OfficerDashboard"),
    path('officer/logout', views.OfficerLogout, name="OfficerLogout"),
]
