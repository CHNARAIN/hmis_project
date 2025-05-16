from django.shortcuts import render, redirect
from .forms import PatientForm
import uuid

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.hospital_id = str(uuid.uuid4())[:8]
            patient.save()
            return render(request, 'registration/success.html', {'patient': patient})
    else:
        form = PatientForm()
    return render(request, 'registration/form.html', {'form': form})
