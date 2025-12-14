<div align="center">

# 🏥 Patient Record Management System

### Modern Medical Records Platform Built with Django

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](LICENSE)

**A comprehensive Django-based web application for managing patient medical records with a modern, trendy purple gradient UI**

[Features](#project-features) • [Installation](#step-by-step-guide-to-run-the-project) • [Usage](#step-10-access-the-application) • [Documentation](docs/) • [Troubleshooting](#troubleshooting)

---

</div>

## ✨ Key Highlights

- 🎨 **Modern UI Design** - Trendy purple gradient theme with smooth animations
- 🔐 **Secure Authentication** - User login, registration, and role-based access
- 📊 **Complete Patient Records** - Medical history, diagnoses, medications, and allergies
- 💊 **Medical-Grade Interface** - Professional admin panel with safety features
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- ⚡ **Real-time Updates** - Dynamic forms with autocomplete and validation
- 🎯 **Safety Features** - Severity warnings, unsaved changes protection
- 🚀 **Easy Setup** - SQLite for development, MySQL for production

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Guide](#step-by-step-guide-to-run-the-project)
- [Features](#project-features)
- [Admin Credentials](#admin-login)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Security](#security-notes)

---

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)
- MySQL 8.0+ or MariaDB 10.6+ (optional, for MySQL database)

## Step-by-Step Guide to Run the Project

### Step 1: Clone or Download the Project

If you haven't already, navigate to the project directory:

```bash
cd "c:\Users\Aldrian Loberiano\Documents\GitHub\Patient_Record_Management_System"
```

### Step 2: Create a Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate.bat
  ```

### Step 3: Install Required Dependencies

Install all required Python packages from requirements.txt:

```bash
python -m pip install -r requirements.txt
```

**Note for Windows users:** If `pip` command is not recognized, always use `python -m pip` instead of just `pip`.

**Dependencies included:**

- Django 5.0.1
- Pillow 10.2.0
- django-crispy-forms 2.1
- crispy-bootstrap5 2024.2
- mysqlclient 2.2.1

### Step 4: Database Configuration

The project is currently configured to use **SQLite** (default), which requires no additional setup.

**Option A: Using SQLite (Default - Recommended for Development)**

- No additional configuration needed
- Database file will be created automatically at `database/db.sqlite3`

**Option B: Using MySQL/MariaDB (Optional)**

1. Install MySQL 8.0+ or MariaDB 10.6+
2. Create a database:
   ```sql
   CREATE DATABASE patient_records_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Update the database configuration in `patient_system/settings.py`:
   - Comment out the SQLite configuration
   - Uncomment the MySQL configuration
   - Update USER, PASSWORD, and other credentials as needed

### Step 5: Create Database Directory (for SQLite)

If using SQLite, create the database directory:

```bash
mkdir database
```

### Step 6: Run Database Migrations

Apply database migrations to create the necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create a Superuser (Admin Account)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set:

- Username
- Email address (optional)
- Password

### Step 8: Collect Static Files (Optional)

If deploying to production, collect static files:

```bash
python manage.py collectstatic
```

### Step 9: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

### Step 10: Access the Application

Open your web browser and navigate to:

- **Main Application:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

**Default Pages:**

- `/` - Dashboard (requires login)
- `/login/` - User login
- `/register/` - User registration
- `/patients/` - Patient list
- `/admin/` - Django admin panel (Trendy Purple Gradient Theme 🎨)

---

## 🔑 Admin Login

**Default Admin Credentials:**

```
Username: admin
Password: admin123
```

> ⚠️ **Important:** Change these credentials in production!

**Admin Features:**

- ✅ Full CRUD operations on all models
- ✅ Medical-grade allergy management interface
- ✅ Modern purple gradient design across all pages
- ✅ Advanced search and filtering
- ✅ Severity badges and visual indicators
- ✅ Autocomplete for medical history selection
- ✅ Patient information preview cards

---

## 🚀 Project Features

### 👥 User Management

- ✅ **Secure Authentication** - Login, logout, and user registration
- ✅ **Role-Based Access** - Custom user roles (Doctor, Nurse, Admin, Receptionist)
- ✅ **Profile Management** - User profiles with phone, specialization, license number

### 📊 Patient Records

- ✅ **Patient Management** - Add, view, edit, and delete patient records
- ✅ **Medical History** - Comprehensive patient medical history tracking
- ✅ **Diagnoses** - Record and manage patient diagnoses with severity levels
- ✅ **Medications** - Track prescribed medications with dosage and schedules
- ✅ **Allergies** - Modern medical-grade allergy management interface

### 🎨 Modern UI/UX

- ✅ **Trendy Purple Gradient Theme** - Vibrant #667eea → #764ba2 gradient design
- ✅ **Animated Interface** - Smooth floating shapes and transitions
- ✅ **Card-Based Design** - Clean white cards with purple accents
- ✅ **Responsive Layout** - Perfect on desktop, tablet, and mobile
- ✅ **Font Awesome Icons** - Professional iconography throughout

### 🔐 Admin Panel (Styled Globally)

- ✅ **Complete UI Transformation** - All admin pages styled with modern theme
- ✅ **Dashboard** - Beautiful gradient background with animated shapes
- ✅ **List Views** - Styled tables with hover effects and gradient headers
- ✅ **Forms** - Modern input fields with purple focus rings
- ✅ **Search & Filters** - Enhanced search bars and filter sidebars
- ✅ **Login Page** - Centered card design with gradient background

### ⚡ Advanced Features

- ✅ **Autocomplete** - Smart suggestions for medical history selection
- ✅ **Severity Warnings** - Visual alerts for critical allergies
- ✅ **Unsaved Changes Protection** - Prevents accidental data loss
- ✅ **Date Auto-population** - Automatic date filling for current entries
- ✅ **Search & Filter** - Advanced filtering on all list views
- ✅ **Pagination** - Smooth navigation through large datasets
- ✅ **Real-time Validation** - Instant feedback on form inputs

### 📱 Technical Features

- ✅ **Django 5.0.1** - Latest stable Django framework
- ✅ **MySQL Support** - Production-ready database integration
- ✅ **SQLite Default** - Quick development setup
- ✅ **Crispy Forms** - Beautiful Bootstrap 5 form rendering
- ✅ **Media Uploads** - Patient photos and document management
- ✅ **Static File Management** - Optimized CSS/JS delivery

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, run the server on a different port:

```bash
python manage.py runserver 8080
```

### Missing Dependencies

If you encounter import errors, ensure all dependencies are installed:

```bash
python -m pip install -r requirements.txt --upgrade
```

### 'pip' is not recognized (Windows)

If you get an error that `pip` is not recognized:

**Solution:** Use `python -m pip` instead of `pip`:

```bash
python -m pip install -r requirements.txt
```

This explicitly runs pip as a Python module, which works even if pip isn't in your system PATH.

### Database Connection Issues (MySQL)

If using MySQL and encountering connection errors:

1. Verify MySQL service is running
2. Check database credentials in `settings.py`
3. Ensure the database exists
4. Verify MySQL/MariaDB version (8.0+/10.6+ required)

### Migration Issues

If migrations fail:

```bash
python manage.py migrate --run-syncdb
```

## Development Notes

- The project uses SQLite by default for easy setup and development
- Static files are served from the `/static/` directory
- Templates are located in the `/templates/` directory
- The `records` app handles all patient record functionality

## Stopping the Server

To stop the development server:

- Press `Ctrl + C` in the terminal

To deactivate the virtual environment:

```bash
deactivate
```

## Additional Commands

### Create new migrations after model changes:

```bash
python manage.py makemigrations
```

### View SQL for migrations:

```bash
python manage.py sqlmigrate records 0001
```

### Run tests:

```bash
python manage.py test
```

### Open Django shell:

```bash
python manage.py shell
```

## Security Notes

⚠️ **Important for Production:**

- Change the `SECRET_KEY` in `settings.py`
- Set `DEBUG = False` in `settings.py`
- Update `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive data
- Use a production-grade database (PostgreSQL/MySQL)
- Configure proper static file serving (WhiteNoise/Nginx)

## License

This project is for educational purposes.
