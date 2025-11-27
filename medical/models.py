from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Department(models.Model):
    """Medical departments model."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    head_doctor = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Doctor(models.Model):
    """Doctor information model."""
    SPECIALIZATION_CHOICES = [
        ('general', 'General Practitioner'),
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('gynecology', 'Gynecology'),
        ('neurology', 'Neurology'),
        ('psychiatry', 'Psychiatry'),
        ('radiology', 'Radiology'),
        ('pathology', 'Pathology'),
        ('anesthesiology', 'Anesthesiology'),
        ('surgery', 'Surgery'),
        ('emergency', 'Emergency Medicine'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    experience_years = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)
    available_days = models.CharField(max_length=100, help_text="Comma-separated days (e.g., Mon,Tue,Wed)")
    available_time_start = models.TimeField(blank=True, null=True)
    available_time_end = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"
    
    @property
    def doctor_name(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Patient(models.Model):
    """Patient information model."""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, default='single')
    address = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    medical_history = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    insurance_provider = models.CharField(max_length=200, blank=True)
    insurance_policy_number = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='patients/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def patient_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class Service(models.Model):
    """Medical services offered model."""
    CATEGORY_CHOICES = [
        ('consultation', 'Consultation'),
        ('diagnostic', 'Diagnostic'),
        ('treatment', 'Treatment'),
        ('surgery', 'Surgery'),
        ('therapy', 'Therapy'),
        ('preventive', 'Preventive Care'),
        ('emergency', 'Emergency'),
        ('laboratory', 'Laboratory'),
        ('radiology', 'Radiology'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField(default=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    requires_appointment = models.BooleanField(default=True)
    preparation_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.category}"
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Appointment(models.Model):
    """Appointment booking model."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('no_show', 'No Show'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    notes = models.TextField(blank=True)
    reason_for_visit = models.TextField()
    symptoms = models.TextField(blank=True)
    cancelled_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.patient_name} - Dr. {self.doctor.last_name} - {self.appointment_date}"
    
    @property
    def patient_name(self):
        return self.patient.patient_name
    
    @property
    def doctor_name(self):
        return self.doctor.doctor_name
    
    def save(self, *args, **kwargs):
        if not self.end_time and self.service:
            from datetime import datetime, timedelta
            start_datetime = datetime.combine(self.appointment_date, self.appointment_time)
            end_datetime = start_datetime + timedelta(minutes=self.service.duration_minutes)
            self.end_time = end_datetime.time()
        super().save(*args, **kwargs)


class MedicalRecord(models.Model):
    """Medical records model."""
    RECORD_TYPES = [
        ('diagnosis', 'Diagnosis'),
        ('prescription', 'Prescription'),
        ('test_result', 'Test Result'),
        ('treatment', 'Treatment'),
        ('consultation', 'Consultation'),
        ('surgery', 'Surgery'),
        ('therapy', 'Therapy'),
        ('emergency', 'Emergency Care'),
    ]
    
    SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
        ('critical', 'Critical'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='medical_records', blank=True, null=True)
    record_type = models.CharField(max_length=20, choices=RECORD_TYPES)
    diagnosis = models.TextField()
    symptoms = models.TextField(blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, blank=True)
    prescription = models.TextField(blank=True)
    treatment_plan = models.TextField(blank=True)
    record_date = models.DateField(default=timezone.now)
    follow_up_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    attachments = models.FileField(upload_to='medical_records/', blank=True, null=True)
    is_confidential = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.patient_name} - {self.record_type} - {self.record_date}"
    
    @property
    def patient_name(self):
        return self.patient.patient_name
    
    @property
    def doctor_name(self):
        return self.doctor.doctor_name


class Prescription(models.Model):
    """Prescription model."""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('paused', 'Paused'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='prescriptions')
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    prescribed_date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    refills_remaining = models.PositiveIntegerField(default=0)
    pharmacy_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.patient_name} - {self.medication_name}"
    
    @property
    def patient_name(self):
        return self.patient.patient_name
    
    @property
    def doctor_name(self):
        return self.doctor.doctor_name


class TestResult(models.Model):
    """Medical test results model."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    RESULT_STATUS_CHOICES = [
        ('normal', 'Normal'),
        ('abnormal', 'Abnormal'),
        ('critical', 'Critical'),
        ('inconclusive', 'Inconclusive'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_results')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='test_results')
    test_name = models.CharField(max_length=200)
    test_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    result_status = models.CharField(max_length=20, choices=RESULT_STATUS_CHOICES, blank=True)
    test_date = models.DateField(default=timezone.now)
    result_date = models.DateField(blank=True, null=True)
    laboratory = models.CharField(max_length=200, blank=True)
    technician = models.CharField(max_length=200, blank=True)
    values = models.JSONField(blank=True, null=True, help_text="Test values in JSON format")
    normal_range = models.CharField(max_length=200, blank=True)
    interpretation = models.TextField(blank=True)
    attachments = models.FileField(upload_to='test_results/', blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.patient_name} - {self.test_name} - {self.test_date}"
    
    @property
    def patient_name(self):
        return self.patient.patient_name
    
    @property
    def doctor_name(self):
        return self.doctor.doctor_name


class Page(models.Model):
    """Static pages model for sitemap."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class ContactMessage(models.Model):
    """Contact form messages model."""
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('archived', 'Archived'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    is_important = models.BooleanField(default=False)
    replied_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']
