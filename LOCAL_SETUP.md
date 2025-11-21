# 🏥 Local Setup Guide - Cavin Otieno Medical Clinic Website

This guide will help you set up and run the Cavin Otieno Medical Clinic website on your local machine.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your machine:

### Required Software
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Code Editor** (VS Code, PyCharm, etc.)

### Optional but Recommended
- **pip** (comes with Python)
- **virtualenv** or **venv** (included in Python 3.3+)
- **GitHub Desktop** (for easier Git operations)

## 🚀 Quick Setup (5 minutes)

Follow these steps to get the website running locally:

### Step 1: Download/Clone the Project

```bash
# If you have the project files
# Extract the clinic folder to your desired location

# Or if cloning from GitHub:
git clone <your-repository-url>
cd clinic
```

### Step 2: Create Virtual Environment

```bash
# Using Python's built-in venv (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install Django and required packages
pip install django pillow

# Or using uv package manager:
# uv add django pillow
```

### Step 4: Setup Database

```bash
# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Optional: Create admin user for backend access
python manage.py createsuperuser
```

### Step 5: Start Development Server

```bash
# Start the server
python manage.py runserver

# The website will be available at:
# http://127.0.0.1:8000
```

### Step 6: Access Your Website

Open your web browser and visit:
- **Main Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin (if you created a superuser)

## 🔧 Detailed Setup Instructions

### Virtual Environment Setup

The virtual environment isolates your project dependencies from other Python projects:

```bash
# Create virtual environment
python -m venv clinic-env

# Activate it
# Windows:
clinic-env\Scripts\activate
# macOS/Linux:
source clinic-env/bin/activate

# When done, deactivate with:
deactivate
```

### Database Configuration

The project uses SQLite by default for development:

```bash
# Check migrations status
python manage.py showmigrations

# If needed, reset database (WARNING: This deletes all data)
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

### Static Files Configuration

The website is configured to serve media files during development:

```bash
# Collect static files (for production)
python manage.py collectstatic

# Development server automatically serves static files
```

## 🌐 Website Sections

Once running, explore these sections:

### Main Pages
- **Homepage** (`/`): Hero section, services overview, testimonials
- **About** (`/about/`): Dr. Cavin Otieno's profile and team information
- **Services** (`/services/`): Comprehensive list of medical services
- **Contact** (`/contact/`): Contact information and inquiry form
- **Appointments** (`/appointments/`): Appointment booking system

### Features to Test
- **Responsive Design**: Test on different screen sizes
- **Contact Forms**: Try the contact and appointment forms
- **WhatsApp Integration**: Test WhatsApp buttons and links
- **Phone Links**: Click phone numbers on mobile devices

## 📱 Testing the Website

### Mobile Testing
1. Open browser developer tools (F12)
2. Toggle device simulation
3. Test various screen sizes
4. Verify touch-friendly interface

### Functionality Testing
1. **Navigation**: Test all menu links
2. **Forms**: Submit contact and appointment forms
3. **External Links**: Verify phone, WhatsApp, and email links
4. **Images**: Check that all images load properly
5. **Responsive Design**: Test on different devices

### Performance Testing
```bash
# Run development server with performance monitoring
python manage.py runserver --debug-toolbar
```

## 🛠️ Development Commands

### Database Operations
```bash
# Make new migrations after model changes
python manage.py makemigrations medical

# Apply migrations
python manage.py migrate

# Reset database (WARNING: Deletes all data)
python manage.py flush

# Create superuser
python manage.py createsuperuser
```

### Development Server
```bash
# Standard server
python manage.py runserver

# Server accessible from network
python manage.py runserver 0.0.0.0:8000

# Custom port
python manage.py runserver 8080

# With debugging
python manage.py runserver --debug-mode
```

### Static Files
```bash
# Collect static files for production
python manage.py collectstatic --noinput

# Check static files configuration
python manage.py findstatic --verbosity 2
```

### Shell Commands
```bash
# Django shell for database operations
python manage.py shell

# Example shell operations:
# from medical.models import *
# Patient.objects.all()
# Appointment.objects.filter(status='confirmed')
```

## 🐛 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

#### Database Errors
```bash
# Reset database
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

#### Static Files Not Loading
1. Check that media files exist in `/media/images/`
2. Verify Django settings for MEDIA_URL and MEDIA_ROOT
3. Restart development server

#### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf venv  # or clinic-env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install django pillow
```

#### Permission Errors (macOS/Linux)
```bash
# Fix file permissions
chmod +x manage.py
```

### Checking System Status
```bash
# Check Django version
python -m django --version

# Check installed packages
pip list

# Check Python path
python -c "import sys; print(sys.path)"
```

## 📁 Project Structure

Understanding the project layout:

```
clinic/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database (auto-created)
├── clinicproject/           # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py            # URL routing
│   └── ...
├── medical/                # Main application
│   ├── models.py          # Data models
│   ├── views.py           # View functions
│   ├── context_processors.py # Global template variables
│   └── ...
├── templates/              # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Homepage
│   └── ...
├── static/                # Static files
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript
│   └── images/          # Static images
└── media/                # Media files (user uploads)
    └── images/          # Clinic images
```

## 🔒 Security Notes

### Development Security
- Default settings are for development only
- Use strong SECRET_KEY for production
- Configure ALLOWED_HOSTS for production
- Never commit sensitive data to version control

### Production Checklist
Before deploying to production:
- [ ] Set DEBUG = False
- [ ] Use strong SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up proper database (PostgreSQL/MySQL)
- [ ] Configure SSL certificate
- [ ] Set up proper static file serving

## 📞 Getting Help

### Support Resources
- **Email**: cavin.otieno012@gmail.com
- **Phone**: +254708101604
- **LinkedIn**: [cavin-otieno-9a841260](https://www.linkedin.com/in/cavin-otieno-9a841260/)
- **Documentation**: Django Documentation, Bootstrap Documentation

### Self-Help Resources
1. **Django Documentation**: https://docs.djangoproject.com/
2. **Bootstrap Documentation**: https://getbootstrap.com/docs/
3. **Python Documentation**: https://docs.python.org/
4. **Stack Overflow**: Search for Django/Python questions

### Common Resources
- **Virtual Environment Issues**: Create new venv and reinstall packages
- **Database Issues**: Delete db.sqlite3 and run migrations again
- **Import Errors**: Check Python path and virtual environment activation
- **Static File Issues**: Verify MEDIA_URL and MEDIA_ROOT settings

## 🎯 Next Steps

After successful setup:

1. **Explore the Admin Panel**: Visit `/admin` and log in with superuser credentials
2. **Customize Content**: Modify templates and add your own content
3. **Add Images**: Replace stock images with your clinic photos
4. **Configure Email**: Set up email settings for contact form functionality
5. **Deploy**: Follow deployment guide for production setup

---

**Happy Coding! 🏥✨**

*This local setup guide ensures you can successfully run the Cavin Otieno Medical Clinic website on your machine for development and testing purposes.*