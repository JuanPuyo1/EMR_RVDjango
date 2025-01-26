
from django.urls import path
from . import views

app_name = "emr"
urlpatterns = [
    path('', views.index, name='index'),
    path('medical_record/', views.medical_record, name='medical_record'),
    path('medication_form/', views.MedCreateView.as_view(), name='medication_form'),
    path('medication_list/', views.MedInventoryView.as_view(), name='medication_list'),
    path('medication_control_list/', views.MedicationControlListView.as_view(), name='medication_control_list'),
    path('medication_control/<str:date>/', views.MedControlRegisterView.as_view(), name='medication_control'),
]
