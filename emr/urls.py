
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('medical_record/', views.medical_record, name='medical_record'),
    path('medication_form/', views.MedCreateView.as_view(), name='medication_form'),
]
