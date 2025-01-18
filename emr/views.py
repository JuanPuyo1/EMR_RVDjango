from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Medication
from .forms import MedicationForm

# Create your views here.

def index(request):
    return render(request, 'emr/index.html')

def medical_record(request):
    return render(request, 'emr/medical_record.html')

class MedCreateView(CreateView):
    template_name = 'emr/medication_form.html'
    form_class = MedicationForm



class MedInventoryView(ListView):
    model = Medication
    template_name = 'emr/medication_list.html'
    context_object_name = 'medications'

