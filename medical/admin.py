"""
Admin configuration for the medical app.
"""

from django.contrib import admin
from .models import Patient, Appointment, MedicalRecord


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin interface for Patient model."""
    list_display = ['first_name', 'last_name', 'phone', 'email', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    list_filter = ['created_at', 'gender']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin interface for Appointment model."""
    list_display = ['patient', 'doctor', 'appointment_date', 'status', 'created_at']
    list_filter = ['status', 'appointment_date', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'doctor']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    """Admin interface for MedicalRecord model."""
    list_display = ['patient', 'record_type', 'record_date', 'created_at']
    list_filter = ['record_type', 'record_date']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_module_permission(self, request):
        """Limit medical records to staff users only."""
        return request.user.is_staff


# Customize admin site header
admin.site.site_header = "Cavin Otieno Medical Clinic Administration"
admin.site.site_title = "Medical Clinic Admin"
admin.site.index_title = "Medical Clinic Management Portal"
