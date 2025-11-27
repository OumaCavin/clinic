"""
Admin configuration for the medical app.
"""

from django.contrib import admin
from .models import (
    Department, Doctor, Patient, Service, Appointment, 
    MedicalRecord, Prescription, TestResult, Page, ContactMessage
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Admin interface for Department model."""
    list_display = ['name', 'head_doctor', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Admin interface for Doctor model."""
    list_display = ['first_name', 'last_name', 'specialization', 'department', 'is_available', 'consultation_fee']
    list_filter = ['specialization', 'department', 'is_available']
    search_fields = ['first_name', 'last_name', 'license_number', 'specialization']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'photo')
        }),
        ('Professional Information', {
            'fields': ('license_number', 'specialization', 'department', 'experience_years', 'bio')
        }),
        ('Availability & Fees', {
            'fields': ('consultation_fee', 'is_available', 'available_days', 'available_time_start', 'available_time_end')
        }),
        ('System Fields', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin interface for Patient model."""
    list_display = ['first_name', 'last_name', 'phone', 'email', 'blood_type', 'is_active', 'created_at']
    list_filter = ['gender', 'blood_type', 'marital_status', 'is_active', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email', 'insurance_policy_number']
    readonly_fields = ['created_at', 'updated_at', 'age']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'blood_type', 'marital_status', 'photo')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')
        }),
        ('Medical Information', {
            'fields': ('medical_history', 'allergies', 'current_medications')
        }),
        ('Insurance', {
            'fields': ('insurance_provider', 'insurance_policy_number')
        }),
        ('System Fields', {
            'fields': ('is_active', 'created_at', 'updated_at', 'age'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for Service model."""
    list_display = ['name', 'category', 'duration_minutes', 'price', 'is_available']
    list_filter = ['category', 'is_available', 'requires_appointment']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin interface for Appointment model."""
    list_display = ['patient', 'doctor', 'service', 'appointment_date', 'appointment_time', 'status', 'priority']
    list_filter = ['status', 'priority', 'appointment_date', 'doctor']
    search_fields = [
        'patient__first_name', 'patient__last_name', 
        'doctor__first_name', 'doctor__last_name', 
        'reason_for_visit'
    ]
    readonly_fields = ['created_at', 'updated_at', 'end_time']
    
    fieldsets = (
        ('Appointment Details', {
            'fields': ('patient', 'doctor', 'service', 'appointment_date', 'appointment_time')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority')
        }),
        ('Visit Information', {
            'fields': ('reason_for_visit', 'symptoms', 'notes')
        }),
        ('System Information', {
            'fields': ('cancelled_reason', 'created_at', 'updated_at', 'end_time'),
            'classes': ('collapse',)
        }),
    )


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    """Admin interface for MedicalRecord model."""
    list_display = ['patient', 'doctor', 'record_type', 'severity', 'record_date', 'created_at']
    list_filter = ['record_type', 'severity', 'record_date', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis', 'treatment_plan']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_module_permission(self, request):
        """Limit medical records to staff users only."""
        return request.user.is_staff
    
    fieldsets = (
        ('Record Information', {
            'fields': ('patient', 'doctor', 'appointment', 'record_type', 'record_date')
        }),
        ('Clinical Information', {
            'fields': ('diagnosis', 'symptoms', 'severity', 'treatment_plan')
        }),
        ('Treatment', {
            'fields': ('prescription', 'follow_up_date')
        }),
        ('Additional Information', {
            'fields': ('notes', 'attachments', 'is_confidential')
        }),
        ('System Fields', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    """Admin interface for Prescription model."""
    list_display = ['patient', 'medication_name', 'doctor', 'status', 'prescribed_date', 'refills_remaining']
    list_filter = ['status', 'prescribed_date', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'medication_name', 'doctor__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_module_permission(self, request):
        """Limit prescriptions to staff users only."""
        return request.user.is_staff


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    """Admin interface for TestResult model."""
    list_display = ['patient', 'test_name', 'test_type', 'status', 'result_status', 'test_date']
    list_filter = ['status', 'result_status', 'test_type', 'test_date', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'test_name', 'interpretation']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_module_permission(self, request):
        """Limit test results to staff users only."""
        return request.user.is_staff


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Admin interface for Page model."""
    list_display = ['title', 'slug', 'is_published', 'is_featured', 'created_at']
    list_filter = ['is_published', 'is_featured', 'created_at']
    search_fields = ['title', 'content', 'meta_keywords']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin interface for ContactMessage model."""
    list_display = ['name', 'email', 'subject', 'status', 'is_important', 'created_at']
    list_filter = ['status', 'is_important', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'phone', 'subject', 'message')
        }),
        ('Status & Importance', {
            'fields': ('status', 'is_important', 'replied_at')
        }),
        ('System Fields', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Customize admin site header
admin.site.site_header = "Cavin Otieno Medical Clinic Administration"
admin.site.site_title = "Medical Clinic Admin"
admin.site.index_title = "Medical Clinic Management Portal"
