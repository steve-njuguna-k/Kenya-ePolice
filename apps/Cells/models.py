from django.db import models
from django.contrib.auth.models import User
from apps.Accused.models import AccusedPerson

CELL_STATUS = [
    ('Occupied', ('Occupied')),
    ('Empty', ('Empty')),
]

# Create your models here.
class Cell(models.Model):
    cell_number = models.CharField(max_length=255, verbose_name='Cell Number.')
    accused_person = models.ForeignKey(AccusedPerson, on_delete=models.CASCADE, verbose_name='Accused Person')
    cell_status = models.CharField(choices=CELL_STATUS, max_length=50, verbose_name='Cell Status')
    occupied_on = models.DateField(verbose_name='Occupied On')
    vaccated_on = models.DateField(verbose_name='Vaccated On')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Police Officer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.cell_number)
    
    class Meta:
        verbose_name_plural = 'Cells'