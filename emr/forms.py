from django import forms
from .models import Medication, MedicationControl
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
            'control_date': forms.DateTimeInput(attrs={'class': 'form-control', 'data-type': 'datetime-local', 'format': '%Y-%m-%dT%H:%M'}),
            'control_location': forms.TextInput(attrs={'class': 'form-control'}),
            'control_observation': forms.TextInput(attrs={'class': 'form-control'}),
        }

