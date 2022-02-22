from django.urls import path
from apps.Cases import views

urlpatterns = [
    path('officer/dashboard/cases', views.OfficerCases, name="OfficerCases"),
    path('case/add', views.AddCase, name="AddCase"),
    path('case/<int:id>/view', views.ViewCaseDetails, name="ViewCaseDetails"),
    path('case/<int:id>/edit', views.EditCase, name="EditCase"),
    path('case/<int:id>/delete', views.DeleteCase, name="DeleteCase"),
]
