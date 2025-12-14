"""
Custom Admin Views - Not using Django's built-in admin
Modern medical-grade admin interface with purple gradient theme
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Patient, MedicalHistory, Diagnosis, Allergy, Medication, CustomUser
from .forms import PatientForm, MedicalHistoryForm, DiagnosisForm, AllergyForm, MedicationForm, ProfileForm


def is_staff_or_admin(user):
    """Check if user is staff or admin"""
    return user.is_authenticated and (user.is_staff or user.role in ['admin', 'doctor'])


@login_required
@user_passes_test(is_staff_or_admin)
def custom_admin_dashboard(request):
    """Custom Admin Dashboard"""
    context = {
        'total_patients': Patient.objects.count(),
        'total_allergies': Allergy.objects.count(),
        'total_diagnoses': Diagnosis.objects.count(),
        'total_medications': Medication.objects.count(),
        'recent_patients': Patient.objects.order_by('-created_at')[:5],
        'critical_allergies': Allergy.objects.filter(severity__in=['severe', 'life_threatening']).order_by('-identified_date')[:5],
        'recent_diagnoses': Diagnosis.objects.order_by('-diagnosis_date')[:5],
    }
    return render(request, 'custom_admin/dashboard.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def patient_list_view(request):
    """List all patients with search and filter"""
    query = request.GET.get('q', '')
    gender_filter = request.GET.get('gender', '')
    blood_filter = request.GET.get('blood_group', '')
    
    patients = Patient.objects.all()
    
    if query:
        patients = patients.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(patient_id__icontains=query) |
            Q(email__icontains=query)
        )
    
    if gender_filter:
        patients = patients.filter(gender=gender_filter)
    
    if blood_filter:
        patients = patients.filter(blood_group=blood_filter)
    
    paginator = Paginator(patients, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'gender_filter': gender_filter,
        'blood_filter': blood_filter,
    }
    return render(request, 'custom_admin/patient_list.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def patient_create_view(request):
    """Create new patient"""
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.first_name} {patient.last_name} created successfully!')
            return redirect('custom_admin:patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'custom_admin/patient_form.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def patient_update_view(request, pk):
    """Update existing patient"""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient {patient.first_name} {patient.last_name} updated successfully!')
            return redirect('custom_admin:patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    context = {'form': form, 'patient': patient, 'action': 'Update'}
    return render(request, 'custom_admin/patient_form.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def patient_detail_view(request, pk):
    """View patient details"""
    patient = get_object_or_404(Patient, pk=pk)
    medical_histories = patient.medical_histories.all().order_by('-date_recorded')
    
    context = {
        'patient': patient,
        'medical_histories': medical_histories,
    }
    return render(request, 'custom_admin/patient_detail.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def patient_delete_view(request, pk):
    """Delete patient"""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        name = f"{patient.first_name} {patient.last_name}"
        patient.delete()
        messages.success(request, f'Patient {name} deleted successfully!')
        return redirect('custom_admin:patient_list')
    
    context = {'patient': patient}
    return render(request, 'custom_admin/patient_confirm_delete.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def allergy_list_view(request):
    """List all allergies with filters"""
    query = request.GET.get('q', '')
    severity_filter = request.GET.get('severity', '')
    
    allergies = Allergy.objects.select_related('medical_history__patient').all()
    
    if query:
        allergies = allergies.filter(
            Q(allergen__icontains=query) |
            Q(reaction__icontains=query) |
            Q(medical_history__patient__first_name__icontains=query) |
            Q(medical_history__patient__last_name__icontains=query)
        )
    
    if severity_filter:
        allergies = allergies.filter(severity=severity_filter)
    
    paginator = Paginator(allergies, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all patients for the modal dropdown
    patients = Patient.objects.all().order_by('first_name', 'last_name')
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'severity_filter': severity_filter,
        'patients': patients,
    }
    return render(request, 'custom_admin/allergy_list.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def allergy_create_view(request):
    """Create new allergy"""
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            allergy = form.save(commit=False)
            patient = form.cleaned_data['patient']
            
            # Get or create a medical history for this patient
            medical_history = MedicalHistory.objects.filter(patient=patient).first()
            if not medical_history:
                medical_history = MedicalHistory.objects.create(
                    patient=patient,
                    recorded_by=request.user,
                    chief_complaint='Allergy record',
                    notes='Created for allergy entry'
                )
            
            allergy.medical_history = medical_history
            allergy.save()
            messages.success(request, f'Allergy record for {allergy.allergen} created successfully!')
            return redirect('custom_admin:allergy_list')
    else:
        form = AllergyForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'custom_admin/allergy_form.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def allergy_update_view(request, pk):
    """Update existing allergy"""
    allergy = get_object_or_404(Allergy, pk=pk)
    
    if request.method == 'POST':
        form = AllergyForm(request.POST, instance=allergy)
        if form.is_valid():
            updated_allergy = form.save(commit=False)
            # Keep the same medical history (patient cannot be changed during edit)
            updated_allergy.medical_history = allergy.medical_history
            updated_allergy.save()
            messages.success(request, f'Allergy record for {allergy.allergen} updated successfully!')
            return redirect('custom_admin:allergy_list')
    else:
        form = AllergyForm(instance=allergy)
    
    context = {'form': form, 'allergy': allergy, 'action': 'Update'}
    return render(request, 'custom_admin/allergy_form.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def allergy_delete_view(request, pk):
    """Delete allergy"""
    allergy = get_object_or_404(Allergy, pk=pk)
    
    if request.method == 'POST':
        allergen = allergy.allergen
        allergy.delete()
        messages.success(request, f'Allergy record for {allergen} deleted successfully!')
        return redirect('custom_admin:allergy_list')
    
    context = {'allergy': allergy}
    return render(request, 'custom_admin/allergy_confirm_delete.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def diagnosis_list_view(request):
    """List all diagnoses"""
    query = request.GET.get('q', '')
    severity_filter = request.GET.get('severity', '')
    
    diagnoses = Diagnosis.objects.select_related('medical_history__patient').all()
    
    # Calculate statistics
    from django.utils import timezone
    from datetime import datetime
    total_count = diagnoses.count()
    unique_patients = diagnoses.values('medical_history__patient').distinct().count()
    current_month = timezone.now().month
    current_year = timezone.now().year
    this_month_count = diagnoses.filter(
        diagnosis_date__year=current_year,
        diagnosis_date__month=current_month
    ).count()
    
    if query:
        diagnoses = diagnoses.filter(
            Q(diagnosis_name__icontains=query) |
            Q(description__icontains=query) |
            Q(icd_code__icontains=query) |
            Q(medical_history__patient__first_name__icontains=query) |
            Q(medical_history__patient__last_name__icontains=query)
        )
    
    if severity_filter:
        diagnoses = diagnoses.filter(severity=severity_filter)
    
    paginator = Paginator(diagnoses, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'severity_filter': severity_filter,
        'total_count': total_count,
        'unique_patients': unique_patients,
        'this_month_count': this_month_count,
    }
    return render(request, 'custom_admin/diagnosis_list.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def medication_list_view(request):
    """List all medications"""
    query = request.GET.get('q', '')
    active_filter = request.GET.get('is_active', '')
    
    medications = Medication.objects.select_related('medical_history__patient', 'prescribed_by').all()
    
    # Calculate statistics
    total_count = medications.count()
    active_count = medications.filter(is_active=True).count()
    unique_patients = medications.values('medical_history__patient').distinct().count()
    
    if query:
        medications = medications.filter(
            Q(medication_name__icontains=query) |
            Q(purpose__icontains=query) |
            Q(medical_history__patient__first_name__icontains=query) |
            Q(medical_history__patient__last_name__icontains=query) |
            Q(prescribed_by__first_name__icontains=query) |
            Q(prescribed_by__last_name__icontains=query)
        )
    
    if active_filter:
        medications = medications.filter(is_active=active_filter == 'true')
    
    paginator = Paginator(medications, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'active_filter': active_filter,
        'total_count': total_count,
        'active_count': active_count,
        'unique_patients': unique_patients,
    }
    return render(request, 'custom_admin/medication_list.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def ajax_patient_search(request):
    """AJAX endpoint for patient search"""
    query = request.GET.get('q', '')
    
    if len(query) < 2:
        return JsonResponse({'results': []})
    
    patients = Patient.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(patient_id__icontains=query)
    )[:10]
    
    results = [{
        'id': p.pk,
        'text': f"{p.first_name} {p.last_name} ({p.patient_id})",
        'patient_id': p.patient_id,
        'name': f"{p.first_name} {p.last_name}"
    } for p in patients]
    
    return JsonResponse({'results': results})


@login_required
@user_passes_test(is_staff_or_admin)
def profile_view(request):
    """View current user's profile"""
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'custom_admin/profile.html', context)


@login_required
@user_passes_test(is_staff_or_admin)
def profile_edit_view(request):
    """Edit current user's profile"""
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('custom_admin:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'custom_admin/profile_edit.html', context)
