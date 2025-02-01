from django import forms
from .models import Medication, MedicationControl, ArterialPressure, TherapyMedicalRecord, Diagnosis, Therapy, FoodDaily, NurseCarerRecord, MedicalRecord
from datetime import datetime


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['med_name', 'med_quantity', 'med_date', 'med_change', 'referer', 'med_observation']

        labels = {
            'med_name': 'Nombre del Medicamento',
            'med_quantity': 'Cantidad Recibida',
            'med_date': 'Fecha de Entrega',
            'med_change': 'Cambio de Medicamento',
            'referer': 'Medico que ordena el Cambio',
            'med_observation': 'Obersavicion (Firma)',
        }
        widgets = {
            'med_name': forms.TextInput(attrs={'class': 'form-control'}),
            'med_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'med_date': forms.DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            'med_change': forms.CheckboxInput(attrs={
            'class': 'form-control',
            'id': 'id_med_change',  
            }
            ),
        'referer': forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_referer',
        }),
            'med_observation': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['med_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")
    

class MedicationControlForm(forms.ModelForm):
    class Meta:
        model = MedicationControl
        fields = ['med', 'control_date', 'control_location', 'control_observation']

        labels = {
            'med': 'Medicamento',
            'control_date': 'Fecha de Control',
            'control_location': 'Ubicación de Control',
            'control_observation': 'Observación',
        }

        widgets = {
            'med': forms.Select(attrs={'class': 'form-control'}),
            'control_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'control_location': forms.TextInput(attrs={'class': 'form-control'}),
            'control_observation': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['med'].queryset = Medication.objects.all().order_by('med_name')
            self.fields['control_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")


class ArterialPressureForm(forms.ModelForm):
    class Meta:
        model = ArterialPressure
        fields = ['arterial_pressure', 'arterial_pressure_date', 'heart_rate', 'saturation', 'temperature', 'observation']

        labels = {
            'arterial_pressure': 'Presión Arterial',
            'arterial_pressure_date': 'Fecha y Hora de Medición',
            'heart_rate': 'Frecuencia Cardiaca',
            'saturation': 'Saturación de Oxígeno',
            'temperature': 'Temperatura',
            'observation': 'Observación',
        }
        placeholders = {
            'arterial_pressure': 'Ejemplo: 180/74mm/HG',
            'arterial_pressure_date': 'Fecha y Hora de Medición',
            'heart_rate': 'Frecuencia Cardiaca',
            'saturation': 'Saturación de Oxígeno',
            'temperature': 'Temperatura',
            'observation': 'Digite su nombre',
        }

        widgets = {
            'arterial_pressure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['arterial_pressure']}),
            'arterial_pressure_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'heart_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['heart_rate']}),
            'saturation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['saturation']}),
            'temperature': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['temperature']}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': placeholders['observation']}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['arterial_pressure_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")



class TherapyMedicalRecordForm(forms.ModelForm):
    class Meta:
        model = TherapyMedicalRecord
        fields = ['diagnosis', 'therapy', 'record_date', 'record_analysis', 'record_therapy', 'record_recommendation', 'record_observation']
        labels = {
            'diagnosis': 'Diagnóstico',
            'therapy': 'Terapia',
            'record_date': 'Fecha de Registro',
            'record_analysis': 'Análisis',
            'record_therapy': 'Tratamiento',
            'record_recommendation': 'Recomendación',
            'record_observation': 'Observación',

        }
        placeholders = {
            'record_recommendation': 'Recomendación',
            'record_observation': 'Agregue observaciones adicionales o escriba su nombre(firma)',
        }
        widgets = {
            'diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'therapy': forms.Select(attrs={'class': 'form-control'}),
            'record_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'record_analysis': forms.Textarea(attrs={'class': 'form-control'}),
            'record_therapy': forms.Textarea(attrs={'class': 'form-control'}),
            'record_recommendation': forms.Textarea(attrs={'class': 'form-control'}),
            'record_observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': placeholders['record_observation']}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['diagnosis'].queryset = Diagnosis.objects.all().order_by('diagnosis_name')
            self.fields['therapy'].queryset = Therapy.objects.all().order_by('therapy_name')
            self.fields['record_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")


class FoodDailyForm(forms.ModelForm):
    class Meta:
        model = FoodDaily
        fields = ['food_daily_type', 'food_daily_date', 'food_daily_food', 'food_daily_observation']

        labels = {
            'food_daily_type': 'Tipo de Comida',
            'food_daily_date': 'Fecha de Comida',
            'food_daily_food': 'Comida',
            'food_daily_observation': 'Observación',
        }

        widgets = {
            'food_daily_type': forms.Select(attrs={'class': 'form-control'}),
            'food_daily_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'food_daily_food': forms.Textarea(attrs={'class': 'form-control'}),
            'food_daily_observation': forms.Textarea(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['food_daily_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")



class NurseCarerRecordForm(forms.ModelForm):
    class Meta:
        model = NurseCarerRecord
        fields = ['nurse_carer_record_type', 
                  'nurse_carer_record_date', 'nurse_carer_record_observation']


        labels = {
           'nurse_carer_record_type': 'Tipo de Registro',
            'nurse_carer_record_date': 'Fecha de Registro',
            'nurse_carer_record_observation': 'Observación',
        }


        widgets = {
            'nurse_carer_record_type': forms.Select(attrs={'class': 'form-control'}),
            'nurse_carer_record_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'nurse_carer_record_observation': forms.Textarea(attrs={'class': 'form-control'}),
        }


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['nurse_carer_record_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")



class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['medical_record_date', 'medical_record_reason', 'medical_record_actual_state', 'medical_record_analysis', 'medical_record_recommendation_plan', 'medical_record_vital_signs']

        labels = {
            'medical_record_date': 'Fecha de Registro',
            'medical_record_reason': 'Motivo de la Consulta',
            'medical_record_actual_state': 'Estado Actual',
            'medical_record_analysis': 'Análisis',
            'medical_record_recommendation_plan': 'Plan de Recomendación',
            'medical_record_vital_signs': 'Signos Vitales',
        }
        placeholders = {
            'medical_record_vital_signs': 'Peso, Talla, Frecuencia Cardiaca, Frecuencia Respiratoria, Temperatura, Saturación de Oxígeno, Presión Arterial',
        }

        widgets = {
            'medical_record_date': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",),
            'medical_record_reason': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_record_actual_state': forms.Textarea(attrs={'class': 'form-control'}),
            'medical_record_analysis': forms.Textarea(attrs={'class': 'form-control'}),
            'medical_record_recommendation_plan': forms.Textarea(attrs={'class': 'form-control'}),
            'medical_record_vital_signs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': placeholders['medical_record_vital_signs']}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['medical_record_date'].initial = datetime.now().strftime("%Y-%m-%dT%H:%M")

