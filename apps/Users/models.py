from django.db import models
from django.contrib.auth.models import User

STATIONS = [
    ("Central Police Station", "Central Police Station"),
    ("Kilimani Police Station", "Kilimani Police Station"),
    ("Embakasi Police Station", "Embakasi Police Station"),
    ("Lang'ata Police Station", "Lang'ata Police Station"),
    ("Ong'ata Rongai Police Station", "Ong'ata Rongai Police Station"),
    ("Buruburu Police Station", "Buruburu Police Station"),
    ("Kasarani Police Station", "Kasarani Police Station"),
    ("Parklands Police Station", "Parklands Police Station"),
    ("Pangani Police Station", "Pangani Police Station"),
    ("Muthaiga Police Station", "Muthaiga Police Station"),
]

# Create your models here.
class OfficerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    middle_name = models.CharField(max_length=10, blank=True, verbose_name='Middle Name')
    bio = models.TextField(max_length=254, blank=True, verbose_name='Bio')
    national_id = models.CharField(max_length=10, blank=True, verbose_name='National ID')
    # profile_picture = CloudinaryField('profile_picture')
    profile_picture = models.ImageField(upload_to='Profile-Pics', verbose_name='Profile-Pics')
    police_station = models.CharField(choices=STATIONS, max_length=150, verbose_name='Police Station', null=True, blank=True)
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        verbose_name_plural = 'Officer Profiles'

class OCSProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    middle_name = models.CharField(max_length=10, blank=True, verbose_name='Middle Name')
    bio = models.TextField(max_length=254, blank=True, verbose_name='Bio')
    national_id = models.CharField(max_length=10, blank=True, verbose_name='National ID')
    # profile_picture = CloudinaryField('profile_picture')
    profile_picture = models.ImageField(upload_to='Profile-Pics', verbose_name='Profile-Pics')
    police_station = models.CharField(choices=STATIONS, max_length=150, verbose_name='Police Station', null=True, blank=True)
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        verbose_name_plural = 'OCS Profiles'