"""
Context processor for site-wide settings
"""
from django.conf import settings

def contact_info(request):
    """
    Add contact information to template context
    """
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Medical Clinic'),
        'site_tagline': getattr(settings, 'SITE_TAGLINE', 'Professional Healthcare'),
        'site_description': getattr(settings, 'SITE_DESCRIPTION', 'Quality healthcare services'),
        'contact_phone': '+254708101604',
        'whatsapp_link': 'wa.me/+254708101604',
        'contact_email': 'cavin.otieno012@gmail.com',
        'linkedin_profile': 'https://www.linkedin.com/in/cavin-otieno-9a841260/',
        'author_name': 'Cavin Otieno',
    }