from django.urls import path
from apps.Accused import views

urlpatterns = [
    path('officer/dashboard/cases', views.OfficerAccused, name="OfficerAccused"),
]
