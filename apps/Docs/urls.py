from django.urls import path
from apps.Docs import views

urlpatterns = [
    path('officer/dashboard/documents', views.OfficerDocs, name="OfficerDocs"),
]
