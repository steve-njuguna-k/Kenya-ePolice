from django.db import models
from Accused.models import AccusedPerson
from Users.models import Profile

VERDICT = [
    ('Guilty', ('Guilty')),
    ('Not Guilty', ('Not Guilty')),
    ('Undetermined', ('Undetermined')),
]

COURTS = [
    ('City Court', ('City Court')),
    ('Milimani Commercial', ('Milimani Commercial')),
    ('Makadara Law Courts', ('Makadara Law Courts')),
    ('Kibera Law Courts', ('Kibera Law Courts')),
    ('Milimani Law Courts', ('Milimani Law Courts')),
    ('Kadhis’ Court – Upperhill', ('Kadhis’ Court – Upperhill')),
    ('JKIA Law Courts', ('JKIA Law Courts')),
]

# Create your models here.
class Court(models.Model):
    court_number = models.CharField(max_length=255, verbose_name='Court Number.')
    accused_person = models.ForeignKey(AccusedPerson, on_delete=models.CASCADE, verbose_name='Accused Person')
    court = models.CharField(choices=COURTS, max_length=255, verbose_name='Court')
    court_verdict = models.CharField(choices=VERDICT, max_length=50, verbose_name='Court Status')
    scheduled_on = models.DateField(verbose_name='Scheduled On')
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Police Officer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.court_number)
    
    class Meta:
        verbose_name_plural = 'Court'