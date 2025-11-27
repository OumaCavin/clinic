# XAMPP Database Setup Guide for Django Clinic Project

## Overview
This guide will help you set up XAMPP (MySQL database) for your Django clinic project. XAMPP provides a complete web server solution stack package containing Apache, MySQL, PHP, and Perl.

## Prerequisites
- XAMPP installed on your system
- Python 3.8+ installed
- Django project already cloned

## Step 1: Install and Configure XAMPP

### 1.1 Install XAMPP
1. Download XAMPP from: https://www.apachefriends.org/
2. Install XAMPP with default settings
3. Start XAMPP Control Panel as Administrator

### 1.2 Start Required Services
1. Open XAMPP Control Panel
2. Start **Apache** (for web server)
3. Start **MySQL** (for database server)
4. Verify both services show "Running" status in green

## Step 2: Create MySQL Database

### 2.1 Access phpMyAdmin
1. Open your web browser
2. Navigate to: `http://localhost/phpmyadmin`
3. You should see the phpMyAdmin interface

### 2.2 Create Database
1. Click on "New" in the left sidebar
2. Enter database name: `clinic_db`
3. Select collation: `utf8mb4_unicode_ci`
4. Click "Create"

### 2.3 Create Database User (Optional but Recommended)
1. Go to "User accounts" tab
2. Click "Add user account"
3. Enter username: `clinic_user`
4. Enter password: `clinic_password123`
5. Select "Create database with same name and grant all privileges"
6. Check "Check all" for Global privileges
7. Click "Go"

## Step 3: Configure Django for MySQL

### 3.1 Update Django Settings
The Django settings are already configured for MySQL in `clinicproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinic_db',
        'USER': 'root',  # or 'clinic_user' if you created a custom user
        'PASSWORD': '',  # or 'clinic_password123' if you created a custom user
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'init_command': "SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci",
        }
    }
}
```

### 3.2 Install MySQL Client
```bash
# In your project directory, install MySQL client
pip install mysqlclient

# Alternative if mysqlclient fails
pip install PyMySQL
```

If using PyMySQL, add this to your `clinicproject/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

## Step 4: Run Database Migrations

### 4.1 Navigate to Project Directory
```bash
cd /path/to/your/clinic/project
```

### 4.2 Create Virtual Environment (if not already created)
```bash
python -m venv clinic_env
```

### 4.3 Activate Virtual Environment
**On Windows:**
```bash
clinic_env\Scripts\activate
```

**On macOS/Linux:**
```bash
source clinic_env/bin/activate
```

### 4.4 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.5 Run Migrations
```bash
python manage.py makemigrations medical
python manage.py migrate
```

### 4.6 Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user for the Django admin interface.

## Step 5: Test the Setup

### 5.1 Start Django Development Server
```bash
python manage.py runserver
```

### 5.2 Access Django Admin
1. Open browser: `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Verify all models are visible and functional

### 5.3 Test Database Connection
1. Go to Django admin
2. Navigate to different sections (Patients, Doctors, Appointments, etc.)
3. Try creating a test record to verify database operations work

## Step 6: Add Sample Data (Optional)

### 6.1 Create Sample Department
1. Go to Django Admin
2. Navigate to "Departments"
3. Add departments like:
   - General Medicine
   - Cardiology
   - Pediatrics
   - Emergency Medicine

### 6.2 Create Sample Doctors
1. Go to "Doctors"
2. Add doctor information with corresponding departments

### 6.3 Create Sample Services
1. Go to "Services"
2. Add medical services offered

## Database Management

### Accessing MySQL Command Line
```bash
# Open XAMPP MySQL command line
mysql -u root -p
```

### Common MySQL Commands
```sql
-- Show databases
SHOW DATABASES;

-- Use clinic database
USE clinic_db;

-- Show tables
SHOW TABLES;

-- Show table structure
DESCRIBE medical_patient;

-- Export database
mysqldump -u root -p clinic_db > clinic_backup.sql

-- Import database
mysql -u root -p clinic_db < clinic_backup.sql
```

## Troubleshooting

### Common Issues and Solutions

#### 1. MySQL Connection Error
**Error:** `django.db.utils.OperationalError: (2002, "Can't connect to server")`
**Solution:** 
- Ensure XAMPP MySQL service is running
- Check if MySQL is using port 3306 (default)
- Verify firewall settings

#### 2. Access Denied Error
**Error:** `Access denied for user 'root'@'localhost'`
**Solution:**
- Reset MySQL root password
- Or create a new user with proper privileges
- Update Django settings with correct credentials

#### 3. mysqlclient Installation Failed
**Error:** `Microsoft Visual C++ 14.0 is required`
**Solution:**
- Install Microsoft C++ Build Tools
- Or use PyMySQL instead:
  ```bash
  pip install PyMySQL
  # Add to clinicproject/__init__.py
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

#### 4. Database Does Not Exist
**Error:** `Unknown database 'clinic_db'`
**Solution:**
- Create the database in phpMyAdmin first
- Verify database name spelling

#### 5. Character Encoding Issues
**Solution:**
- Ensure database uses `utf8mb4_unicode_ci` collation
- Django settings already include proper charset configuration

## Security Considerations

### 1. Change Default Passwords
- Change MySQL root password from empty
- Use strong passwords for database users

### 2. Configure Firewall
- Allow only necessary ports (3306 for MySQL if remote access needed)
- Restrict access to localhost for development

### 3. Environment Variables
Consider using environment variables for sensitive data:
```python
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'clinic_db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}
```

## Backup and Maintenance

### 1. Regular Backups
```bash
# Create backup
mysqldump -u root -p clinic_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

### 2. Database Monitoring
- Check MySQL logs in XAMPP: `xampp/mysql/data/mysql_error.log`
- Monitor database size
- Regularly update MySQL and Django

## Next Steps

1. **Configure Production Settings:** Update Django settings for production deployment
2. **Add User Authentication:** Implement patient and doctor login systems
3. **Create API Endpoints:** Build REST API for mobile apps
4. **Implement Reporting:** Add statistical reports and analytics
5. **Set Up Email Notifications:** Configure email for appointment reminders

## Support

If you encounter issues:
1. Check XAMPP control panel for error messages
2. Review Django error logs
3. Verify MySQL error logs
4. Consult Django and MySQL documentation

---

**Note:** This setup is configured for local development. For production, consider using a dedicated MySQL server and implementing proper security measures.