from django import forms
from .models import Medication
from datetime import datetime
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['med_name', 'med_quantity', 'med_date', 'med_change', 'referer', 'med_observation']

        widgets = {
            'med_name': forms.TextInput(attrs={'class': 'form-control'}),
            'med_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'med_date': forms.DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            'med_change': forms.TextInput(attrs={'class': 'form-control'}),
            'referer': forms.TextInput(attrs={'class': 'form-control'}),
            'med_observation': forms.TextInput(attrs={'class': 'form-control'}),
        }

        exclude = ['patient']
    

