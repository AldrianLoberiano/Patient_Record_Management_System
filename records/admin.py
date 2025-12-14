from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
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
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone']
    search_fields = ['patient_id', 'first_name', 'last_name', 'email']
    list_filter = ['gender', 'blood_group']
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_recorded', 'recorded_by']
    list_filter = ['date_recorded']
    search_fields = ['patient__first_name', 'patient__last_name', 'patient__patient_id', 'notes']
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['medical_history', 'diagnosis_name', 'diagnosis_date', 'severity']
    list_filter = ['severity', 'diagnosis_date']
    search_fields = ['diagnosis_name', 'description']
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    change_form_template = 'admin/records/allergy_change_form.html'
    list_display = ['get_patient_name', 'allergen', 'severity_badge', 'identified_date', 'reaction_preview']
    list_filter = ['severity', 'identified_date']
    search_fields = ['allergen', 'reaction', 'medical_history__patient__first_name', 'medical_history__patient__last_name']
    readonly_fields = ['get_patient_info']
    autocomplete_fields = ['medical_history']
    date_hierarchy = 'identified_date'
    
    fieldsets = (
        ('Patient & Medical History', {
            'fields': ('medical_history', 'get_patient_info'),
            'classes': ('wide',),
        }),
        ('Allergy Details', {
            'fields': ('allergen', 'reaction', 'severity', 'identified_date'),
            'classes': ('wide',),
        }),
        ('Clinical Notes', {
            'fields': ('notes',),
            'classes': ('wide', 'collapse'),
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
    
    def get_patient_name(self, obj):
        patient = obj.medical_history.patient
        return f"{patient.first_name} {patient.last_name}"
    get_patient_name.short_description = 'Patient'
    get_patient_name.admin_order_field = 'medical_history__patient__last_name'
    
    def severity_badge(self, obj):
        colors = {
            'mild': '#4caf50',
            'moderate': '#ff9800',
            'severe': '#f44336',
            'life_threatening': '#d32f2f'
        }
        color = colors.get(obj.severity, '#666')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 11px; text-transform: uppercase;">{}</span>',
            color,
            obj.get_severity_display()
        )
    severity_badge.short_description = 'Severity'
    severity_badge.admin_order_field = 'severity'
    
    def reaction_preview(self, obj):
        if len(obj.reaction) > 50:
            return obj.reaction[:50] + '...'
        return obj.reaction
    reaction_preview.short_description = 'Reaction'
    
    def get_patient_info(self, obj):
        if obj.pk:
            patient = obj.medical_history.patient
            return format_html(
                '<div style="background: #f0f0f0; padding: 15px; border-radius: 8px; margin: 10px 0;">'
                '<strong style="font-size: 16px;">Patient: {}</strong><br>'
                '<span style="color: #666;">DOB: {} | ID: {} | Blood: {}</span>'
                '</div>',
                f"{patient.first_name} {patient.last_name}",
                patient.date_of_birth.strftime('%B %d, %Y'),
                patient.patient_id,
                patient.blood_group or 'Not recorded'
            )
        return "Select a medical history record to see patient information"
    get_patient_info.short_description = 'Patient Information'

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['medical_history', 'medication_name', 'dosage', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['medication_name', 'purpose']
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

# Register CustomUser with custom admin
admin.site.register(CustomUser, CustomUserAdmin)
