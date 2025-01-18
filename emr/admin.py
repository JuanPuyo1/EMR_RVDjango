from django.contrib import admin
from .models import Patient, MedicalRecord, Medication, ArterialPressure, MedicationControl, FoodControl, WeightControl

admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Medication)
admin.site.register(ArterialPressure)
admin.site.register(MedicationControl)
admin.site.register(FoodControl)
admin.site.register(WeightControl)
