from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Medication, Patient
from .forms import MedicationForm

# Create your views here.

def index(request):
    return render(request, 'emr/index.html')

def medical_record(request):
    return render(request, 'emr/medical_record.html')

class MedCreateView(CreateView):
    template_name = 'emr/medication_form.html'
    form_class = MedicationForm

    def form_valid(self, form):
        patient = Patient.objects.get(id=1)
        form.instance.patient = patient
        return redirect('emr:medication_list')



class MedInventoryView(ListView):
    model = Medication
    template_name = 'emr/medication_list.html'
    context_object_name = 'medications'

