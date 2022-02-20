from django.contrib import admin
from apps.Users.models import OCSProfile, OfficerProfile

# Register your models here.
admin.site.register(OCSProfile)
admin.site.register(OfficerProfile)