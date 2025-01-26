from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View
from .models import Medication, Patient, MedicationControl
from .forms import MedicationForm, MedicationControlForm
from datetime import date, timedelta

# Create your views here.

def index(request):
    return render(request, 'emr/index.html')

def medical_record(request):
    return render(request, 'emr/medical_record.html')

'''

Medication Inventory

'''

class MedCreateView(CreateView):
    template_name = 'emr/medication_inventory_form.html'
    form_class = MedicationForm

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(id=1)
        form.save()
        return redirect('emr:medication_inventory')



class MedInventoryView(ListView):
    model = Medication
    template_name = 'emr/medication_inventory.html'
    context_object_name = 'medications'


'''
Medication Control List

'''

class MedControlView(View):
    template_name = 'emr/medication_control_list.html'
    
    def get(self, request):
        # Get week offset from query parameters, default to 0 (current week)
        week_offset = int(request.GET.get('week', 0))
        print(week_offset)
        # Calculate the date range for the requested week
        today = date.today()
        base_monday = today - timedelta(days=today.weekday())  # Get current week's Monday
        start_of_week = base_monday + timedelta(weeks=week_offset)
        print(start_of_week)
        end_of_week = start_of_week + timedelta(days=6)  # Friday (4 days after Monday)
        print(end_of_week)
        # Get all medications
        medications = Medication.objects.all()
        print(medications)
        # Get records for the specified week
        records = MedicationControl.objects.filter(
            control_date__range=(start_of_week, end_of_week)
        )
        print(records)
        # Organize records by day
        weekly_data = {day: [] for day in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]}
        for record in records:
            weekday = record.control_date.weekday()
            if weekday < 5:  # Only process Monday through Friday
                weekly_data[list(weekly_data.keys())[weekday]].append(record)
        
        # Format dates for display
        week_display = {
            'start': start_of_week.strftime('%d/%m/%Y'),
            'end': end_of_week.strftime('%d/%m/%Y'),
            'offset': week_offset
        }
        
        context = {
            'medications': medications,
            'weekly_data': weekly_data,
            'week_display': week_display
        }
        
        return render(request, self.template_name, context)
    

class MedControlDetailsView(View):
    template_name = 'emr/medication_control_details.html'
    def get(self, request, record_id):
        record = MedicationControl.objects.get(id=record_id)
        return render(request, self.template_name, {'record': record})

class MedControlFormView(View):
    form_class = MedicationControlForm
    template_name = 'emr/medication_control_form.html'
    def get(self, request):      
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emr:medication_control_list')