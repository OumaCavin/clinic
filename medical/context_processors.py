"""
Context processor for site-wide settings
"""
from django.conf import settings

def site_settings(request):
    """
    Add site settings to template context
    """
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Medical Clinic'),
        'site_tagline': getattr(settings, 'SITE_TAGLINE', 'Professional Healthcare'),
        'site_description': getattr(settings, 'SITE_DESCRIPTION', 'Quality healthcare services'),
        'contact_phone': '+254708101604',
        'whatsapp_link': 'wa.me/+254708101604',
        'contact_email': 'cavin.otieno012@gmail.com',
        'author_name': 'Cavin Otieno',
    }