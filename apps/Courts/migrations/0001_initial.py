# Generated by Django 3.1.8 on 2022-02-23 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accused', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_number', models.CharField(max_length=255, verbose_name='Court Number.')),
                ('court', models.CharField(choices=[('City Court', 'City Court'), ('Milimani Commercial', 'Milimani Commercial'), ('Makadara Law Courts', 'Makadara Law Courts'), ('Kibera Law Courts', 'Kibera Law Courts'), ('Milimani Law Courts', 'Milimani Law Courts'), ('Kadhis’ Court – Upperhill', 'Kadhis’ Court – Upperhill'), ('JKIA Law Courts', 'JKIA Law Courts')], max_length=255, verbose_name='Court')),
                ('court_verdict', models.CharField(choices=[('Guilty', 'Guilty'), ('Not Guilty', 'Not Guilty'), ('Undetermined', 'Undetermined')], max_length=50, verbose_name='Court Status')),
                ('scheduled_on', models.DateField(verbose_name='Scheduled On')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('accused_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accused.accusedperson', verbose_name='Accused Person')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.profile', verbose_name='Police Officer')),
            ],
            options={
                'verbose_name_plural': 'Court',
            },
        ),
    ]
