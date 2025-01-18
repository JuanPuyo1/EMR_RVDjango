from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    USERNAME_FIELD = 'id'
    def __str__(self):
        return self.phone

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateField()
    record_description = models.TextField()
    
class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=100)
    med_quantity = models.IntegerField()
    med_date = models.DateField()
    med_change = models.TextField()
    referer = models.ForeignKey(User, on_delete=models.CASCADE)
    med_observation = models.TextField()

class ArterialPressure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    arterial_pressure = models.IntegerField()
    arterial_pressure_date = models.DateField()
    arterial_pressure_time = models.TimeField()
    heart_rate = models.IntegerField()
    saturation = models.IntegerField()
    temperature = models.IntegerField()
    observation = models.TextField()

class MedicationControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med = models.ForeignKey(Medication, on_delete=models.CASCADE)
    control_date = models.DateField()
    control_time = models.TimeField()
    control_location = models.CharField(max_length=100)
    control_observation = models.TextField()

class FoodControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_date = models.DateField()
    food_time = models.TimeField()
    food_location = models.CharField(max_length=100)
    food_observation = models.TextField()

class WeightControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.IntegerField()
    weight_date = models.DateField()
    weight_time = models.TimeField()
    weight_observation = models.TextField()

