# Generated by Django 5.1.4 on 2025-01-18 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0004_alter_medication_referer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
    ]
