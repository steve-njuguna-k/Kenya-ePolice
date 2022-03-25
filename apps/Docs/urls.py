from django.urls import path
from Docs import views

urlpatterns = [
    path('officer/dashboard/documents', views.OfficerDocs, name="OfficerDocs"),
]
