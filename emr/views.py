from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'emr/index.html')

def medical_record(request):
    return render(request, 'emr/medical_record.html')

