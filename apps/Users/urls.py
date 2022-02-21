from django.urls import path
from apps.Users import views
from django.conf.urls.static import static
from Core import settings

urlpatterns = [
    path('', views.Home, name="Home"),
    path('register', views.Register, name="Register"),
    path('login', views.Login, name="Login"),
    path('activateuser/<uidb64>/<token>',views.ActivateAccount, name = 'ActivateAccount'),
    path('officer/dashboard', views.OfficerDashboard, name="OfficerDashboard"),
    path('ocs/dashboard', views.OCSDashboard, name="OCSDashboard"),
    path('logout', views.Logout, name="Logout"),
    path('profile/settings', views.Settings, name="Settings"),
    path('profile/edit', views.EditProfile, name="EditProfile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
