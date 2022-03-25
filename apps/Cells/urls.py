from django.urls import path
from Cells import views

urlpatterns = [
    path('officer/dashboard/cells', views.OfficerCells, name="OfficerCells"),
    path('cell/add', views.AddCellInfo, name="AddCellInfo"),
    path('cell/<int:id>/view', views.ViewCellDetails, name="ViewCellDetails"),
    path('cell/<int:id>/edit', views.EditCellInfo, name="EditCellInfo"),
    path('cell/<int:id>/delete', views.DeleteCellInfo, name="DeleteCellInfo"),
]
