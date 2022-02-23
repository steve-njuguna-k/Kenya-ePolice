from django.db import models

# Create your models here.
class Docs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    # doc_upload = CloudinaryField('doc_upload')
    doc_upload = models.FileField(upload_to='Doc-Uploads', verbose_name='Document Upload')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'Documents'