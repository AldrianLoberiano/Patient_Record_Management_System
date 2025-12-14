from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import CustomUser, Patient, MedicalHistory, Diagnosis, Allergy, Medication
from .forms import (CustomUserCreationForm, LoginForm, PatientForm, 
                    MedicalHistoryForm, DiagnosisForm, AllergyForm, MedicationForm)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('custom_admin:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('custom_admin:dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'records/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'records/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_doctors': CustomUser.objects.filter(role='doctor').count(),
        'total_nurses': CustomUser.objects.filter(role='nurse').count(),
        'recent_patients': Patient.objects.all()[:5],
        'total_records': MedicalHistory.objects.count(),
    }
    return render(request, 'records/dashboard.html', context)


@login_required
def patient_list(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(patient_id__icontains=query) |
            Q(phone__icontains=query)
        )
    else:
        patients = Patient.objects.all()
    
    return render(request, 'records/patient_list.html', {'patients': patients, 'query': query})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    medical_histories = patient.medical_histories.all()
    
    # Get all diagnoses, allergies, and medications
    all_diagnoses = Diagnosis.objects.filter(medical_history__patient=patient)
    all_allergies = Allergy.objects.filter(medical_history__patient=patient)
    all_medications = Medication.objects.filter(medical_history__patient=patient, is_active=True)
    
    context = {
        'patient': patient,
        'medical_histories': medical_histories,
        'all_diagnoses': all_diagnoses,
        'all_allergies': all_allergies,
        'all_medications': all_medications,
    }
    return render(request, 'records/patient_detail.html', context)


@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.registered_by = request.user
            patient.save()
            messages.success(request, f'Patient {patient.patient_id} registered successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    return render(request, 'records/patient_form.html', {'form': form, 'title': 'Register New Patient'})


@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient information updated successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'records/patient_form.html', {'form': form, 'title': 'Update Patient', 'patient': patient})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient record deleted successfully!')
        return redirect('patient_list')
    
    return render(request, 'records/patient_confirm_delete.html', {'patient': patient})


@login_required
def medical_history_create(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_history = form.save(commit=False)
            medical_history.patient = patient
            medical_history.recorded_by = request.user
            medical_history.save()
            messages.success(request, 'Medical history recorded successfully!')
            return redirect('medical_history_detail', pk=medical_history.pk)
    else:
        form = MedicalHistoryForm()
    
    return render(request, 'records/medical_history_form.html', {
        'form': form, 
        'patient': patient,
        'title': 'Add Medical History'
    })


@login_required
def medical_history_detail(request, pk):
    medical_history = get_object_or_404(MedicalHistory, pk=pk)
    diagnoses = medical_history.diagnoses.all()
    allergies = medical_history.allergies.all()
    medications = medical_history.medications.all()
    
    context = {
        'medical_history': medical_history,
        'diagnoses': diagnoses,
        'allergies': allergies,
        'medications': medications,
    }
    return render(request, 'records/medical_history_detail.html', context)


@login_required
def add_diagnosis(request, history_pk):
    medical_history = get_object_or_404(MedicalHistory, pk=history_pk)
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            diagnosis = form.save(commit=False)
            diagnosis.medical_history = medical_history
            diagnosis.save()
            messages.success(request, 'Diagnosis added successfully!')
            return redirect('medical_history_detail', pk=medical_history.pk)
    else:
        form = DiagnosisForm()
    
    return render(request, 'records/diagnosis_form.html', {
        'form': form,
        'medical_history': medical_history,
        'title': 'Add Diagnosis'
    })


@login_required
def add_allergy(request, history_pk):
    medical_history = get_object_or_404(MedicalHistory, pk=history_pk)
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            allergy = form.save(commit=False)
            allergy.medical_history = medical_history
            allergy.save()
            messages.success(request, 'Allergy added successfully!')
            return redirect('medical_history_detail', pk=medical_history.pk)
    else:
        form = AllergyForm()
    
    return render(request, 'records/allergy_form.html', {
        'form': form,
        'medical_history': medical_history,
        'title': 'Add Allergy'
    })


@login_required
def add_medication(request, history_pk):
    medical_history = get_object_or_404(MedicalHistory, pk=history_pk)
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.medical_history = medical_history
            medication.prescribed_by = request.user
            medication.save()
            messages.success(request, 'Medication added successfully!')
            return redirect('medical_history_detail', pk=medical_history.pk)
    else:
        form = MedicationForm()
    
    return render(request, 'records/medication_form.html', {
        'form': form,
        'medical_history': medical_history,
        'title': 'Add Medication'
    })
