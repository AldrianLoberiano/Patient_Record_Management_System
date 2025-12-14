"""
Custom Admin URLs - Separate from Django's built-in admin
"""

from django.urls import path
from . import admin_views

app_name = 'custom_admin'

urlpatterns = [
    # Dashboard
    path('', admin_views.custom_admin_dashboard, name='dashboard'),
    
    # Patient Management
    path('patients/', admin_views.patient_list_view, name='patient_list'),
    path('patients/create/', admin_views.patient_create_view, name='patient_create'),
    path('patients/<int:pk>/', admin_views.patient_detail_view, name='patient_detail'),
    path('patients/<int:pk>/update/', admin_views.patient_update_view, name='patient_update'),
    path('patients/<int:pk>/delete/', admin_views.patient_delete_view, name='patient_delete'),
    
    # Allergy Management
    path('allergies/', admin_views.allergy_list_view, name='allergy_list'),
    path('allergies/create/', admin_views.allergy_create_view, name='allergy_create'),
    path('allergies/<int:pk>/update/', admin_views.allergy_update_view, name='allergy_update'),
    path('allergies/<int:pk>/delete/', admin_views.allergy_delete_view, name='allergy_delete'),
    
    # Diagnosis Management
    path('diagnoses/', admin_views.diagnosis_list_view, name='diagnosis_list'),
    path('diagnoses/create/', admin_views.diagnosis_create_view, name='diagnosis_create'),
    
    # Medication Management
    path('medications/', admin_views.medication_list_view, name='medication_list'),
    
    # AJAX Endpoints
    path('ajax/patient-search/', admin_views.ajax_patient_search, name='ajax_patient_search'),
    
    # Profile Management
    path('profile/', admin_views.profile_view, name='profile'),
    path('profile/edit/', admin_views.profile_edit_view, name='profile_edit'),
]
