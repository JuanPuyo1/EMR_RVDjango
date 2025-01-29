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

class Diagnosis(models.Model):
    diagnosis_name = models.CharField(max_length=100)
    diagnosis_description = models.TextField()

    def __str__(self):
        return self.diagnosis_name
    
class Therapy(models.Model):
    therapy_name = models.CharField(max_length=100)
    therapy_description = models.TextField()

    def __str__(self):
        return self.therapy_name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.DO_NOTHING, null=True, blank=True)
    therapy = models.ForeignKey(Therapy, on_delete=models.DO_NOTHING, null=True, blank=True)
    record_analysis = models.TextField(null=True, blank=True)  
    record_therapy = models.TextField(null=True, blank=True)
    record_recommendation = models.TextField(null=True, blank=True)
    record_observation = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return self.diagnosis.diagnosis_name + " " + self.record_date.strftime('%d/%m/%Y')

    
class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    med_name = models.CharField(max_length=100)
    med_quantity = models.CharField(max_length=100)
    med_date = models.DateTimeField()
    med_change = models.BooleanField(default=False)
    referer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    med_observation = models.TextField()

class ArterialPressure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    arterial_pressure = models.CharField(max_length=100)
    arterial_pressure_date = models.DateTimeField()
    heart_rate = models.CharField(max_length=100)
    saturation = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    observation = models.TextField()

class MedicationControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    med = models.ForeignKey(Medication, on_delete=models.DO_NOTHING)
    control_date = models.DateTimeField()
    control_location = models.CharField(max_length=100)
    control_observation = models.TextField()


class FoodIngestion(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    food_date = models.DateTimeField()
    food_ingestion = models.CharField(max_length=100, null=True, blank=True)
    food_eliminated = models.CharField(max_length=100, null=True, blank=True)
    food_observation = models.TextField()

    def __str__(self):
        return self.food_ingestion + " " + self.food_date.strftime('%d/%m/%Y')

class FoodControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    food_control_name = models.CharField(max_length=100)
    food_control_date = models.DateTimeField()
    food_control_location = models.CharField(max_length=100)
    food_control_observation = models.TextField()

class WeightControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    weight = models.IntegerField()
    weight_date = models.DateTimeField()
    weight_observation = models.TextField()

