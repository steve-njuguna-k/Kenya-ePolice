from django.urls import path
from apps.Accused import views

urlpatterns = [
    path('officer/dashboard/arested', views.OfficerAccused, name="OfficerAccused"),
]
