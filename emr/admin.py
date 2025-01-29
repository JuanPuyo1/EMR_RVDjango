from django.contrib import admin
from .models import Patient, MedicalRecord, Diagnosis, Therapy, Medication, ArterialPressure, MedicationControl, FoodControl, WeightControl, FoodIngestion

admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Diagnosis)
admin.site.register(Therapy)
admin.site.register(Medication)
admin.site.register(ArterialPressure)

admin.site.register(MedicationControl)
admin.site.register(FoodControl)
admin.site.register(FoodIngestion)
admin.site.register(WeightControl)
