# Generated by Django 4.1.3 on 2022-12-10 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='designationFlag',
            field=models.CharField(blank=True, choices=[('Project Manager', 'Project Manger'), ('Employee', 'Employee')], default='Employee', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='userProfile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmpDetails', to=settings.AUTH_USER_MODEL),
        ),
    ]
