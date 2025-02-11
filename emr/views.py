from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View, UpdateView 
from django.urls import reverse_lazy
from .models import Medication, Patient, MedicationControl, ArterialPressure, FoodIngestion, TherapyMedicalRecord, FoodDaily, NurseCarerRecord, MedicalRecord, TherapyMedicalValoration
from .forms import MedicationForm, MedicationControlForm, ArterialPressureForm, TherapyMedicalRecordForm, FoodDailyForm, NurseCarerRecordForm, MedicalRecordForm, TherapyMedicalValorationForm, FoodIngestionForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required(login_url='accounts/login/')
def index(request):

    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        if patient_id:
            request.session['current_patient_id'] = patient_id


    patients = Patient.objects.all()
    current_patient_id = request.session.get('current_patient_id')
    
    context = {
        'patients': patients,
        'current_patient_id': current_patient_id
    }
    return render(request, 'emr/index.html', context)


'''
Patient Mixin

'''

class PatientRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        patient_id = request.session.get('current_patient_id')
        if not patient_id:
            messages.error(request, 'Por favor seleccione un paciente primero')
            return redirect('emr:index')
        try:
            self.patient = Patient.objects.get(id=patient_id)
            return super().dispatch(request, *args, **kwargs)
        except Patient.DoesNotExist:
            messages.error(request, 'Paciente no encontrado')
            return redirect('emr:index')

'''

TO Medical Record

'''


class TherapyMedicalRecordView(PatientRequiredMixin, View):
    template_name = 'emr/therapy_medical_record_list.html'
    context_object_name = 'medical_records'

    def get(self, request):
        medical_records = TherapyMedicalRecord.objects.filter(patient=self.patient).order_by('-record_date')
        context = {
            'medical_records': medical_records,
            'patient': self.patient
        }
        return render(request, self.template_name, context)

class TherapyMedicalRecordFormView(PatientRequiredMixin, View):
    form_class = TherapyMedicalRecordForm
    template_name = 'emr/therapy_medical_record_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:medical_record_list')


class TherapyMedicalRecordUpdateFormView(PatientRequiredMixin, UpdateView):

    model = TherapyMedicalRecord  
    form_class = TherapyMedicalRecordForm
    template_name = 'emr/therapy_medical_record_form.html'
    success_url = reverse_lazy('emr:therapy_medical_record_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.patient
        return context


class TherapyMedicalValorationView(PatientRequiredMixin, View):
    template_name = 'emr/therapy_valoration_list.html'
    context_object_name = 'therapy_medical_valoration'

    def get(self, request):
        print(self.patient)
        therapy_medical_valoration = TherapyMedicalValoration.objects.filter(patient=self.patient).order_by('-therapy_medical_valoration_date')
        return render(request, self.template_name, {'therapy_medical_valoration': therapy_medical_valoration, 'patient': self.patient})


class TherapyMedicalValorationFormView(PatientRequiredMixin, View):
    form_class = TherapyMedicalValorationForm
    template_name = 'emr/therapy_valoration_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})

'''

Medication Inventory

'''



class MedCreateView(PatientRequiredMixin, CreateView):
    template_name = 'emr/medication_inventory_form.html'
    form_class = MedicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.patient
        return context

    def form_valid(self, form):
        form.instance.patient = self.patient
        form.save()
        return redirect('emr:medication_inventory')




class MedInventoryView(PatientRequiredMixin, View):
    template_name = 'emr/medication_inventory.html'
    def get(self, request):
        medications = Medication.objects.filter(patient=self.patient)
        context = {
            'medications': medications,
            'patient': self.patient
        }
        return render(request, self.template_name, context)




'''
Medication Control List

'''

class MedControlView(PatientRequiredMixin, View):
    template_name = 'emr/medication_control_list.html'
    
    def get(self, request):
        # Get week offset from query parameters, default to 0 (current week)
        week_offset = int(request.GET.get('week', 0))
        # Calculate the date range for the requested week
        today = date.today()
        base_monday = today - timedelta(days=today.weekday())  # Get current week's Monday
        start_of_week = base_monday + timedelta(weeks=week_offset)
        end_of_week = start_of_week + timedelta(days=6)  # Friday (4 days after Monday)
        
        # Get all medications
        medications = Medication.objects.all()
        # Get records for the specified week
        records = MedicationControl.objects.filter(
            control_date__range=(start_of_week, end_of_week),
            patient=self.patient
        )
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
            'week_display': week_display,
            'patient': self.patient
        }
        
        return render(request, self.template_name, context)
    

class MedControlDetailsView(View):
    template_name = 'emr/medication_control_details.html'
    def get(self, request, record_id):
        record = MedicationControl.objects.get(id=record_id)
        return render(request, self.template_name, {'record': record})

class MedControlFormView(PatientRequiredMixin, View):
    form_class = MedicationControlForm
    template_name = 'emr/medication_control_form.html'
    def get(self, request):      
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:medication_control_list')
        


'''
    Arterial Pressure   

'''

class ArterialPressureView(PatientRequiredMixin, View):
        
    template_name = 'emr/arterial_pressure_list.html'
    

    def get(self, request):
        arterial_pressures = ArterialPressure.objects.filter(patient=self.patient).order_by('-arterial_pressure_date')
        context = {
            'arterial_pressures': arterial_pressures,
            'patient': self.patient
        }
        return render(request, self.template_name, context)

class ArterialPressureFormView(PatientRequiredMixin, View):
    form_class = ArterialPressureForm
    template_name = 'emr/arterial_pressure_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:arterial_pressure_list')


'''

Food Ingestion
'''

class FoodIngestionView(PatientRequiredMixin, View):
    template_name = 'emr/food_ingestion_list.html'
    def get(self, request):
        
        today = date.today()
      
        day_offset = int(request.GET.get('day', 0))
        base_monday = today - timedelta(days=today.weekday()) 
        start_of_day = base_monday + timedelta(days=day_offset)
        end_of_day = start_of_day + timedelta(days=1)
        

        day_display = {
            'start': start_of_day.strftime('%d/%m/%Y'),
            'end': end_of_day.strftime('%d/%m/%Y'),
            'offset': day_offset
        }


        records = FoodIngestion.objects.filter(
            food_date__range=(start_of_day, end_of_day),
            patient=self.patient
        )
        print(records)
        context = {
            'records': records,
            'day_display': day_display,
            'patient': self.patient
        }

        return render(request, self.template_name, context)
    

class FoodIngestionFormView(PatientRequiredMixin, View):
    form_class = FoodIngestionForm
    template_name = 'emr/food_ingestion_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:food_ingestion_list')

'''

Food Daily

'''

class FoodDailyView(PatientRequiredMixin, View):
    template_name = 'emr/food_daily_list.html'
    def get(self, request):


        today = date.today()
        day_offset = int(request.GET.get('day', 0))
        base_monday = today - timedelta(days=today.weekday()) 
        start_of_day = base_monday + timedelta(days=day_offset)
        end_of_day = start_of_day + timedelta(days=1)
            

        day_display = {
            'start': start_of_day.strftime('%d/%m/%Y'),
            'end': end_of_day.strftime('%d/%m/%Y'),
            'offset': day_offset
        }
        records = FoodDaily.objects.filter(
            patient=self.patient,
            food_daily_date__range=(start_of_day, end_of_day)
        )

        context = {
            'records': records,
            'day_display': day_display,
            'patient': self.patient
        }
        return render(request, self.template_name, context)
    

class FoodDailyFormView(PatientRequiredMixin, View):
    form_class = FoodDailyForm
    template_name = 'emr/food_daily_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:food_daily_list')


'''

Nurse Carer Record

'''

class NurseCarerRecordView(PatientRequiredMixin, View):
    template_name = 'emr/nurse_carer_record_list.html'
    def get(self, request):
        patient_id = request.session.get('current_patient_id')
        patient = Patient.objects.get(id=patient_id)

        today = date.today()
        day_offset = int(request.GET.get('day', 0))
        base_monday = today - timedelta(days=today.weekday()) 
        start_of_day = base_monday + timedelta(days=day_offset)
        end_of_day = start_of_day + timedelta(days=1)
            

        day_display = {
            'start': start_of_day.strftime('%d/%m/%Y'),
            'end': end_of_day.strftime('%d/%m/%Y'),
            'offset': day_offset
        }
        records = NurseCarerRecord.objects.filter(
            patient_id=patient_id,
            nurse_carer_record_date__range=(start_of_day, end_of_day)
        )
        context = {
            'records': records,
            'day_display': day_display,
            'patient': patient
        }
        return render(request, self.template_name, context)
    


class NurseCarerRecordFormView(PatientRequiredMixin, View):
    form_class = NurseCarerRecordForm
    template_name = 'emr/nurse_carer_record_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:nurse_carer_record_list')

'''

Medical Record

'''


class MedicalRecordView(PatientRequiredMixin, View):
    template_name = 'emr/medical_record_list.html'
    context_object_name = 'medical_records'
    def get(self, request):
        medical_records = MedicalRecord.objects.filter(patient=self.patient).order_by('-medical_record_date')
        context = {
            'medical_records': medical_records,
            'patient': self.patient
        }
        return render(request, self.template_name, context)


class MedicalRecordDetailView(PatientRequiredMixin, View):
    template_name = 'emr/medical_record_detail.html'
    def get(self, request, medical_record_id):
        medical_record = MedicalRecord.objects.get(id=medical_record_id)
        return render(request, self.template_name, {'medical_record': medical_record})

class MedicalRecordUpdateView(PatientRequiredMixin, UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'emr/medical_record_form.html'
    success_url = reverse_lazy('emr:medical_record_list')

class MedicalRecordFormView(PatientRequiredMixin, View):
    form_class = MedicalRecordForm
    template_name = 'emr/medical_record_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'patient': self.patient})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            form.instance.patient = self.patient
            form.save()
            return redirect('emr:medical_record_list')


