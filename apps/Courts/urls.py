from django.urls import path
from Courts import views

urlpatterns = [
    path('officer/dashboard/court/info', views.OfficerCourtInfo, name="OfficerCourtInfo"),
    path('court/info/add', views.AddCourtInfo, name="AddCourtInfo"),
    path('court/info/<int:id>/view', views.ViewCourtInfoDetails, name="ViewCourtInfoDetails"),
    path('court/info/<int:id>/edit', views.EditCourtInfo, name="EditCourtInfo"),
    path('court/info/<int:id>/delete', views.DeleteCourtInfo, name="DeleteCourtInfo"),
]
