from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View
from .models import Medication, Patient, MedicationControl
from .forms import MedicationForm, MedicationControlForm

# Create your views here.

def index(request):
    return render(request, 'emr/index.html')

def medical_record(request):
    return render(request, 'emr/medical_record.html')

class MedCreateView(CreateView):
    template_name = 'emr/medication_form.html'
    form_class = MedicationForm

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(id=1)
        form.save()
        return redirect('emr:medication_list')



class MedInventoryView(ListView):
    model = Medication
    template_name = 'emr/medication_list.html'
    context_object_name = 'medications'




class MedControlView(View):
    def get(self, request):
        return render(request, 'emr/medication_inventory.html')
    

class MedControlRegisterView(View):
    form_class = MedicationControlForm
    def get(self, request, date ):
        medications = Medication.objects.all()
        form = self.form_class()

        return render(request, 'emr/medication_control.html', {'medications': medications, 'form': form})


class MedicationControlListView(ListView):
    model = MedicationControl
    template_name = 'emr/medication_control_list.html'
    context_object_name = 'medications'


