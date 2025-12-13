from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    specialization = models.CharField(max_length=100, blank=True, help_text="Medical specialization (for doctors)")
    license_number = models.CharField(max_length=50, blank=True, unique=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    patient_id = models.CharField(max_length=20, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='patient_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    registered_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='registered_patients')
    
    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = f"PAT{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-created_at']


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    date_recorded = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    chief_complaint = models.TextField(help_text="Main reason for visit")
    vital_signs = models.JSONField(blank=True, null=True, help_text="Blood pressure, temperature, etc.")
    physical_examination = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient.patient_id} - {self.date_recorded.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-date_recorded']
        verbose_name_plural = "Medical Histories"


class Diagnosis(models.Model):
    SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
        ('critical', 'Critical'),
    ]
    
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='diagnoses')
    diagnosis_name = models.CharField(max_length=200)
    diagnosis_date = models.DateField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    description = models.TextField()
    icd_code = models.CharField(max_length=20, blank=True, help_text="ICD-10 code")
    status = models.CharField(max_length=50, default='active')
    
    def __str__(self):
        return f"{self.diagnosis_name} - {self.severity}"
    
    class Meta:
        verbose_name_plural = "Diagnoses"
        ordering = ['-diagnosis_date']


class Allergy(models.Model):
    SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
        ('life_threatening', 'Life Threatening'),
    ]
    
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='allergies')
    allergen = models.CharField(max_length=200)
    reaction = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    identified_date = models.DateField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.allergen} - {self.severity}"
    
    class Meta:
        verbose_name_plural = "Allergies"
        ordering = ['-identified_date']


class Medication(models.Model):
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='medications')
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100, help_text="e.g., twice daily, every 8 hours")
    route = models.CharField(max_length=50, default='oral', help_text="e.g., oral, IV, topical")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    purpose = models.TextField()
    side_effects = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    prescribed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.medication_name} - {self.dosage}"
    
    class Meta:
        ordering = ['-start_date']
