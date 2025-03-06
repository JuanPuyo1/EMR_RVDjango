
from django.urls import path
from . import views

app_name = "emr"
urlpatterns = [
    path('', views.index, name='index'),
    path('medical_record_list/', views.MedicalRecordView.as_view(), name='medical_record_list'),
    path('medical_record_form/', views.MedicalRecordFormView.as_view(), name='medical_record_form'),
    path('medical_record_detail/<int:medical_record_id>/', views.MedicalRecordDetailView.as_view(), name='medical_record_detail'),

    path('therapy_medical_record_list/', views.TherapyMedicalRecordView.as_view(), name='therapy_medical_record_list'),
    path('therapy_medical_record_form/', views.TherapyMedicalRecordFormView.as_view(), name='therapy_medical_record_form'),
    path('therapy_medical_record_form/<int:pk>/', views.TherapyMedicalRecordUpdateFormView.as_view(), name='therapy_medical_record_form_update'),

    path('therapy_valoration_list/', views.TherapyMedicalValorationView.as_view(), name='therapy_valoration_list'),
    path('therapy_valoration_form/', views.TherapyMedicalValorationFormView.as_view(), name='therapy_valoration_form'),


    path('medication_form/', views.MedCreateView.as_view(), name='medication_form'),
    path('medication_inventory/', views.MedInventoryView.as_view(), name='medication_inventory'),
    path('medication_inventory/<int:pk>/', views.MedUpdateView.as_view(), name='medication_update'),
    path('medication_inventory/<int:pk>/delete/', views.MedDeleteView.as_view(), name='medication_delete'),
   
    path('medication_control_form/', views.MedControlFormView.as_view(), name='medication_control_form'),

    path('medication_control_details/<int:record_id>/', views.MedControlDetailsView.as_view(), name='medication_control_details'),
    path('medication_control_list/', views.MedControlView.as_view(), name='medication_control_list'),


    path('arterial_pressure_form/', views.ArterialPressureFormView.as_view(), name='arterial_pressure_form'),
    path('arterial_pressure_list/', views.ArterialPressureView.as_view(), name='arterial_pressure_list'),
    path('arterial_pressure_form/<int:pk>/', views.ArterialPressureUpdateView.as_view(), name='arterial_pressure_update'),
    path('arterial_pressure_form/<int:pk>/delete/', views.ArterialPressureDeleteView.as_view(), name='arterial_pressure_delete'),

    path('food_ingestion_list/', views.FoodIngestionView.as_view(), name='food_ingestion_list'),
    path('food_ingestion_form/', views.FoodIngestionFormView.as_view(), name='food_ingestion_form'),
    path('food_ingestion_form/<int:pk>/', views.FoodIngestionUpdateView.as_view(), name='food_ingestion_update'),
    path('food_ingestion_form/<int:pk>/delete/', views.FoodIngestionDeleteView.as_view(), name='food_ingestion_delete'),
    
    path('food_daily_list/', views.FoodDailyView.as_view(), name='food_daily_list'),
    path('food_daily_form/', views.FoodDailyFormView.as_view(), name='food_daily_form'),

    path('nurse_carer_record_list/', views.NurseCarerRecordView.as_view(), name='nurse_carer_record_list'),
    path('nurse_carer_record_form/', views.NurseCarerRecordFormView.as_view(), name='nurse_carer_record_form'), 
    ]
