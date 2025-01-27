from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    record_description = models.TextField()
    
class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=100)
    med_quantity = models.CharField(max_length=100)
    med_date = models.DateTimeField()
    med_change = models.BooleanField(default=False)
    referer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    med_observation = models.TextField()

class ArterialPressure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    arterial_pressure = models.CharField(max_length=100)
    arterial_pressure_date = models.DateTimeField()
    heart_rate = models.CharField(max_length=100)
    saturation = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    observation = models.TextField()

class MedicationControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med = models.ForeignKey(Medication, on_delete=models.CASCADE)
    control_date = models.DateTimeField()
    control_location = models.CharField(max_length=100)
    control_observation = models.TextField()

class FoodControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_date = models.DateTimeField()
    food_location = models.CharField(max_length=100)
    food_observation = models.TextField()

class WeightControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.IntegerField()
    weight_date = models.DateTimeField()
    weight_observation = models.TextField()

