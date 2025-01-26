
from django.urls import path
from . import views

app_name = "emr"
urlpatterns = [
    path('', views.index, name='index'),
    path('medical_record/', views.medical_record, name='medical_record'),
    path('medication_form/', views.MedCreateView.as_view(), name='medication_form'),
    path('medication_inventory/', views.MedInventoryView.as_view(), name='medication_inventory'),
    path('medication_control_form/', views.MedControlFormView.as_view(), name='medication_control_form'),
    path('medication_control_details/<int:record_id>/', views.MedControlDetailsView.as_view(), name='medication_control_details'),
    path('medication_control_list/', views.MedControlView.as_view(), name='medication_control_list'),
]
