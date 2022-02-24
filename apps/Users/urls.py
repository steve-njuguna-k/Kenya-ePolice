from django.urls import path
from apps.Users import views
from django.conf.urls.static import static
from Core import settings

urlpatterns = [
    path('', views.Home, name="Home"),
    
    # Auth URLs
    path('register', views.Register, name="Register"),
    path('login', views.Login, name="Login"),
    path('logout', views.Logout, name="Logout"),
    path('activateuser/<uidb64>/<token>',views.ActivateAccount, name = 'ActivateAccount'),

    # Officer Dashboard URLs
    path('officer/dashboard', views.OfficerDashboard, name="OfficerDashboard"),
    path('officer/dashboard/profile/settings', views.OfficerSettings, name="OfficerSettings"),
    path('officer/dashboard/profile/edit', views.OfficerEditProfile, name="OfficerEditProfile"),
    path('officer/dashboard/profile', views.OfficerProfile, name="OfficerProfile"),

    # Officer Dashboard URLs
    path('ocs/dashboard', views.OCSDashboard, name="OCSDashboard"),

    # Search
    path('officer/dashboard/search', views.Search, name="Search"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
