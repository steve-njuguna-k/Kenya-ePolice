import imp
from django.urls import path
from apps.Users import views

urlpatterns = [
    path('get-started', views.GetStarted, name="GetStarted")
]
