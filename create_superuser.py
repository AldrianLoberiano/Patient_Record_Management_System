import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patient_system.settings')
django.setup()

from records.models import CustomUser

# Create superuser
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not CustomUser.objects.filter(username=username).exists():
    CustomUser.objects.create_superuser(
        username=username, 
        email=email, 
        password=password,
        role='admin',
        first_name='Admin',
        last_name='User'
    )
    print("Superuser created successfully!")
    print(f"Username: {username}")
    print(f"Password: {password}")
else:
    print(f"User '{username}' already exists")
    user = CustomUser.objects.get(username=username)
    user.set_password(password)
    user.role = 'admin'
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("Password updated for existing user!")
    print(f"Username: {username}")
    print(f"Password: {password}")
