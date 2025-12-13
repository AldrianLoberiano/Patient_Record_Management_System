from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    # Medical History URLs
    path('patients/<int:patient_pk>/medical-history/new/', views.medical_history_create, name='medical_history_create'),
    path('medical-history/<int:pk>/', views.medical_history_detail, name='medical_history_detail'),
    
    # Diagnosis, Allergy, Medication URLs
    path('medical-history/<int:history_pk>/diagnosis/add/', views.add_diagnosis, name='add_diagnosis'),
    path('medical-history/<int:history_pk>/allergy/add/', views.add_allergy, name='add_allergy'),
    path('medical-history/<int:history_pk>/medication/add/', views.add_medication, name='add_medication'),
]
