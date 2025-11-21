"""
Utility functions for the medical app.
"""

import datetime
from django.core.mail import send_mail
from django.conf import settings


def send_appointment_email(appointment, user_email):
    """Send appointment confirmation email."""
    subject = f'Appointment Confirmation - {settings.SITE_NAME}'
    message = f'''
    Dear {appointment.patient_name},
    
    Your appointment has been scheduled for:
    Date: {appointment.appointment_date}
    Time: {appointment.appointment_time}
    Doctor: {appointment.doctor}
    
    Please arrive 15 minutes early for your appointment.
    
    For any questions, contact us at {settings.CONTACT_EMAIL} or {settings.CONTACT_PHONE}.
    
    Best regards,
    {settings.SITE_NAME}
    '''
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])


def format_phone_number(phone):
    """Format phone number for display."""
    if phone.startswith('+'):
        return phone
    elif phone.startswith('0'):
        return '+254' + phone[1:]
    else:
        return '+254' + phone


def calculate_age(birth_date):
    """Calculate age from birth date."""
    today = datetime.date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def get_business_hours():
    """Return clinic business hours."""
    return {
        'monday': '8:00 AM - 5:00 PM',
        'tuesday': '8:00 AM - 5:00 PM', 
        'wednesday': '8:00 AM - 5:00 PM',
        'thursday': '8:00 AM - 5:00 PM',
        'friday': '8:00 AM - 5:00 PM',
        'saturday': '9:00 AM - 2:00 PM',
        'sunday': 'Emergency Only'
    }


def is_business_hours():
    """Check if current time is within business hours."""
    now = datetime.datetime.now()
    weekday = now.weekday()  # 0=Monday, 6=Sunday
    current_time = now.time()
    
    hours = get_business_hours()
    
    if weekday == 6:  # Sunday
        return False
    
    if weekday == 5:  # Saturday
        business_start = datetime.time(9, 0)   # 9:00 AM
        business_end = datetime.time(14, 0)    # 2:00 PM
        return business_start <= current_time <= business_end
    
    # Monday to Friday
    business_start = datetime.time(8, 0)   # 8:00 AM
    business_end = datetime.time(17, 0)    # 5:00 PM
    return business_start <= current_time <= business_end