from django.db import models
from Accused.models import AccusedPerson
from Users.models import Profile

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

COUNTIES = [
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CRIME = [
    ('Arson', ('Arson')),
    ('Armed Robbery', ('Armed Robbery')),
    ('Assault', ('Assault')),
    ('Burglary', ('Burglary')),
    ('Carjacking', ('Carjacking')),
    ('Cattle Rustling', ('Cattle Rustling')),
    ('Corruption', ('Corruption')),
    ('Drug Abuse', ('Drug Abuse')),
    ('Drug Trafficking', ('Drug Trafficking')),
    ('Embezzlement', ('Embezzlement')),
    ('Fraud', ('Fraud')),
    ('Homicide', ('Homicide')),
    ('Human trafficking', ('Human trafficking')),
    ('Kidnapping', ('Kidnapping')),
    ('Mob Justice', ('Mob Justice')),
    ('Money Laundering', ('Money Laundering')),
    ('Massive Looting', ('Massive Looting')),
    ('Petty Theft', ('Petty Theft')),
    ('Pickpocketing', ('Pickpocketing')),
    ('Rape', ('Rape')),
    ('Terrorism', ('Terrorism')),
]

CASE_STATUS = [
    ('Not Started', ('Not Started')),
    ('Ongoing', ('Ongoing')),
    ('Complete', ('Complete')),
]

# Create your models here.
class Case(models.Model):
    case_number = models.CharField(max_length=255, verbose_name='Arrest Number.')
    accused_person = models.ForeignKey(AccusedPerson, on_delete=models.CASCADE, verbose_name='Accused Person')
    cause_of_arrest = models.TextField(max_length=254, verbose_name='Cause Of Arrest')
    crime_category = models.CharField(choices=CRIME, max_length=50, verbose_name='Crime Category')
    arrest_location = models.CharField(max_length=50, verbose_name='Arrest Location')
    case_started_on = models.DateField(verbose_name='Case Started On')
    case_concluded_on = models.DateField(verbose_name='Case Concluded On', null=True, blank=True)
    case_status = models.CharField(choices=CASE_STATUS, max_length=50, verbose_name='Case Status')
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Police Officer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.accused_person.first_name + ' ' + self.accused_person.middle_name + ' ' + self.accused_person.last_name)
    
    class Meta:
        verbose_name_plural = 'Cases'