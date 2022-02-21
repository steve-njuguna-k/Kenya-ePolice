from django.urls import path
from apps.Accused import views

urlpatterns = [
    path('officer/dashboard/arested', views.OfficerAccused, name="OfficerAccused"),
    path('accused/person/<int:id>/view', views.ViewArrestedPersonDetails, name="ViewArrestedPersonDetails"),
    path('accused/person/<int:id>/delete', views.DeleteArrestedPersonDetails, name="DeleteArrestedPersonDetails"),
]
