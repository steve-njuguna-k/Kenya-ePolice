from django.db import models
from apps.Users.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Shift(models.Model):
    police_officer = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Police Officer')
    start_time = models.DateTimeField(verbose_name='Start Time & Day')
    stop_time = models.DateTimeField(verbose_name='Stop Time & Day')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OCS Officer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.police_officer.user.username + ' - ' + self.police_officer.user.first_name + ' ' + self.police_officer.middle_name + ' ' + self.police_officer.user.last_name)
    
    class Meta:
        verbose_name_plural = 'Shifts'