from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """Home page view"""
    context = {
        'title': 'Home',
        'hero_title': 'Professional Healthcare Services in Kenya',
        'hero_subtitle': 'Quality medical care by Cavin Otieno and team',
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us',
        'about_title': 'Meet Dr. Cavin Otieno',
        'about_content': """Dr. Cavin Otieno is a dedicated medical professional with years of experience in providing quality healthcare services in Kenya. 
        Our clinic is committed to delivering personalized, compassionate care to every patient who walks through our doors.

        With a focus on modern medical practices and patient-centered care, we ensure that every individual receives the attention and treatment they deserve. 
        Our team of qualified medical professionals work tirelessly to maintain the highest standards of healthcare in our community.""",
    }
    return render(request, 'about.html', context)

def services(request):
    """Services page view"""
    context = {
        'title': 'Our Services',
        'services': [
            {
                'title': 'General Consultations',
                'description': 'Comprehensive medical consultations for all ages',
                'icon': 'stethoscope'
            },
            {
                'title': 'Preventive Care',
                'description': 'Regular health checkups and screenings',
                'icon': 'shield'
            },
            {
                'title': 'Pediatric Care',
                'description': 'Specialized healthcare for children',
                'icon': 'baby'
            },
            {
                'title': 'Emergency Care',
                'description': '24/7 emergency medical services',
                'icon': 'ambulance'
            },
            {
                'title': 'Chronic Disease Management',
                'description': 'Ongoing care for chronic conditions',
                'icon': 'heart'
            },
            {
                'title': 'Laboratory Services',
                'description': 'Comprehensive diagnostic testing',
                'icon': 'flask'
            }
        ]
    }
    return render(request, 'services.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Contact Us',
        'contact_info': {
            'phone': '+254708101604',
            'whatsapp': 'wa.me/+254708101604',
            'email': 'cavin.otieno012@gmail.com',
            'address': 'Nairobi, Kenya',
            'hours': 'Monday - Friday: 8:00 AM - 6:00 PM\nSaturday: 9:00 AM - 4:00 PM\nSunday: Emergency Only'
        }
    }
    return render(request, 'contact.html', context)

def appointments(request):
    """Appointments page view"""
    context = {
        'title': 'Book Appointment',
        'appointment_text': 'Schedule your appointment with our healthcare professionals',
    }
    return render(request, 'appointments.html', context)
