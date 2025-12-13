from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Patient, MedicalHistory, Diagnosis, Allergy, Medication

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role', 'phone', 'specialization', 'license_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role', 'phone', 'specialization', 'license_number')}),
    )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone']
    search_fields = ['patient_id', 'first_name', 'last_name', 'email']
    list_filter = ['gender', 'blood_group']

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_recorded', 'recorded_by']
    list_filter = ['date_recorded']
    search_fields = ['patient__first_name', 'patient__last_name', 'notes']

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['medical_history', 'diagnosis_name', 'diagnosis_date', 'severity']
    list_filter = ['severity', 'diagnosis_date']
    search_fields = ['diagnosis_name', 'description']

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ['medical_history', 'allergen', 'severity', 'identified_date']
    list_filter = ['severity', 'identified_date']
    search_fields = ['allergen', 'reaction']

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['medical_history', 'medication_name', 'dosage', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['medication_name', 'purpose']

# Register CustomUser with custom admin
admin.site.register(CustomUser, CustomUserAdmin)
