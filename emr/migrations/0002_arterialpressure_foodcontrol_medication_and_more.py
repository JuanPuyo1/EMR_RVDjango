# Generated by Django 5.1.4 on 2025-01-18 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArterialPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arterial_pressure', models.IntegerField()),
                ('arterial_pressure_date', models.DateField()),
                ('arterial_pressure_time', models.TimeField()),
                ('heart_rate', models.IntegerField()),
                ('saturation', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('observation', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FoodControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('food_date', models.DateField()),
                ('food_time', models.TimeField()),
                ('food_location', models.CharField(max_length=100)),
                ('food_observation', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=100)),
                ('med_quantity', models.IntegerField()),
                ('med_date', models.DateField()),
                ('med_change', models.TextField()),
                ('med_observation', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('referer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicationControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_date', models.DateField()),
                ('control_time', models.TimeField()),
                ('control_location', models.CharField(max_length=100)),
                ('control_observation', models.TextField()),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='WeightControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('weight_date', models.DateField()),
                ('weight_time', models.TimeField()),
                ('weight_observation', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
