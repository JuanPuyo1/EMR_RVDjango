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


class TherapyMedicalValoration(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    therapy_medical_valoration_date = models.DateTimeField()
    therapy_medical_valoration_reason = models.CharField(max_length=100)
    therapy_medical_valoration_diagnostic = models.CharField(max_length=100)
    therapy_medical_valoration_analysis = models.TextField()
    therapy_medical_valoration_treatment_plan = models.TextField()
    therapy_medical_valoration_observation = models.TextField()

    def __str__(self):
        return self.therapy_medical_valoration_date.strftime('%d/%m/%Y')

class TherapyMedicalRecord(models.Model):
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
    med_presentation = models.CharField(max_length=100, null=True, blank=True)
    med_quantity = models.CharField(max_length=100)
    med_date = models.DateTimeField()
    med_change = models.BooleanField(default=False)
    referer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    med_observation = models.TextField()

    def __str__(self):
        return self.med_name + " " + self.med_presentation + " " + self.med_quantity

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

    def __str__(self):
        return self.med.med_name + " " + self.control_date.strftime('%d/%m/%Y')

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


class FoodDailyType(models.Model):
    food_daily_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.food_daily_type_name

class FoodDaily(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    food_daily_date = models.DateTimeField()
    food_daily_type = models.ForeignKey(FoodDailyType, on_delete=models.DO_NOTHING)
    food_daily_food = models.TextField()
    food_daily_observation = models.TextField()

    def __str__(self):
        return self.food_daily_type.food_daily_type_name + " " + self.food_daily_date.strftime('%d/%m/%Y')

class WeightControl(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    weight = models.IntegerField()
    weight_date = models.DateTimeField()
    weight_observation = models.TextField()



class NurseCarerRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    nurse_carer_record_type = models.CharField(max_length=30, null=True, blank=True, choices=[
        ('Registro de enfermería', 'Registro de enfermería'),
        ('Registro de cuidador', 'Registro de cuidador'),
    ])

    nurse_carer_record_date = models.DateTimeField()
    nurse_carer_record_observation = models.TextField()

    def __str__(self):
        return self.nurse_carer_record_type + " " + self.nurse_carer_record_date.strftime('%d/%m/%Y')


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    medical_record_date = models.DateTimeField()
    medical_record_reason = models.CharField(max_length=100)
    medical_record_actual_state = models.TextField()
    medical_record_analysis = models.TextField()
    medical_record_recommendation_plan = models.TextField()
    medical_record_vital_signs = models.TextField()
