# Generated by Django 5.1.4 on 2025-01-31 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0013_nursecarerrecord'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicalRecord',
            new_name='TherapyMedicalRecord',
        ),
    ]
