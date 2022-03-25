from django.urls import path
from Accused import views
from django.conf.urls.static import static
from Core import settings

urlpatterns = [
    path('officer/dashboard/arested', views.OfficerAccused, name="OfficerAccused"),
    path('accused/person/add', views.AddArrestedPerson, name="AddArrestedPerson"),
    path('accused/person/<int:id>/view', views.ViewArrestedPersonDetails, name="ViewArrestedPersonDetails"),
    path('accused/person/<int:id>/edit', views.EditArrestedPerson, name="EditArrestedPerson"),
    path('accused/person/<int:id>/delete', views.DeleteArrestedPersonDetails, name="DeleteArrestedPersonDetails"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
