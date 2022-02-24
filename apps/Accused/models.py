from django.db import models
from apps.Users.models import Profile

GENDER = [
    ('Male', ('Male')),
    ('Female', ('Female')),
]

ARREST_STATUS = [
    ('Free', ('Free')),
    ('Convicted', ('Convicted')),
    ('In Custody', ('In Custody')),
    ('Out On Bond', ('Out On Bond')),
    ('Out On Cash Bail', ('Out On Cash Bail')),
]

# Create your models here.
class AccusedPerson(models.Model):
    arrest_number = models.CharField(max_length=255, verbose_name='Arrest Number.')
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    middle_name = models.CharField(max_length=100, verbose_name='Middle Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    date_of_birth = models.DateField(verbose_name='Date Of Birth')
    gender = models.CharField(choices=GENDER, max_length=10, verbose_name='Gender')
    national_id = models.CharField(max_length=10, verbose_name='National ID')
    # profile_picture = CloudinaryField('accused_persons_profile_picture')
    profile_picture = models.ImageField(upload_to='Accused-Profile-Pics', verbose_name='Accused Person Profile Pics')
    arrest_status = models.CharField(choices=ARREST_STATUS, max_length=50, verbose_name='Arrest Status')
    arrested_on = models.DateField(verbose_name='Arrested On')
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Police Officer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.first_name + ' ' + self.middle_name + ' ' + self.last_name)
    
    class Meta:
        verbose_name_plural = 'Accused Persons Profiles'