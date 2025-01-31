
from django.urls import path
from . import views

app_name = "emr"
urlpatterns = [
    path('', views.index, name='index'),
    path('medical_record_list/', views.MedicalRecordView.as_view(), name='medical_record_list'),
    path('medical_record_form/', views.MedicalRecordFormView.as_view(), name='medical_record_form'),
    path('medical_record_form/<int:pk>/', views.MedicalRecordUpdateFormView.as_view(), name='medical_record_form_update'),


    path('medication_form/', views.MedCreateView.as_view(), name='medication_form'),
    path('medication_inventory/', views.MedInventoryView.as_view(), name='medication_inventory'),
    path('medication_control_form/', views.MedControlFormView.as_view(), name='medication_control_form'),
    path('medication_control_details/<int:record_id>/', views.MedControlDetailsView.as_view(), name='medication_control_details'),
    path('medication_control_list/', views.MedControlView.as_view(), name='medication_control_list'),


    path('arterial_pressure_form/', views.ArterialPressureFormView.as_view(), name='arterial_pressure_form'),
    path('arterial_pressure_list/', views.ArterialPressureView.as_view(), name='arterial_pressure_list'),


    path('food_ingestion_list/', views.FoodIngestionView.as_view(), name='food_ingestion_list'),

    path('food_daily_list/', views.FoodDailyView.as_view(), name='food_daily_list'),
    path('food_daily_form/', views.FoodDailyFormView.as_view(), name='food_daily_form'),
    ]
