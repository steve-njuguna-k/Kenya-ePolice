from django.urls import path
from apps.Shifts import views

urlpatterns = [
    path('officer/dashboard/shifts', views.OfficerShifts, name="OfficerShifts"),
]
