from django.contrib import admin
from .models import Patient, TherapyMedicalRecord, Diagnosis, Therapy, Medication, ArterialPressure, MedicationControl, FoodControl, WeightControl, FoodIngestion, FoodDaily, FoodDailyType, MedicalRecord

admin.site.register(Patient)
admin.site.register(TherapyMedicalRecord)
admin.site.register(MedicalRecord)  
admin.site.register(Diagnosis)
admin.site.register(Therapy)
admin.site.register(Medication)
admin.site.register(ArterialPressure)
admin.site.register(FoodDaily)
admin.site.register(FoodDailyType)
admin.site.register(MedicationControl)
admin.site.register(FoodControl)
admin.site.register(FoodIngestion)
admin.site.register(WeightControl)
