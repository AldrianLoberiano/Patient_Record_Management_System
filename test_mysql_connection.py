"""
MySQL Connection Test Script
Tests if MySQL database is accessible and properly configured.
"""

import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pymysql
    print("✓ pymysql is installed")
except ImportError:
    print("✗ pymysql not installed")

try:
    import MySQLdb
    print("✓ mysqlclient is installed")
except ImportError:
    print("✗ mysqlclient not installed")

print("\nAttempting to connect to MySQL...")

try:
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patient_system.settings')
    django.setup()
    
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ Successfully connected to MySQL!")
        print(f"✓ MySQL Version: {version[0]}")
        
        cursor.execute("SELECT DATABASE()")
        db = cursor.fetchone()
        print(f"✓ Current Database: {db[0]}")
        
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"✓ Number of tables: {len(tables)}")
        
        if tables:
            print("\nExisting tables:")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("\nNo tables found. Run 'python manage.py migrate' to create them.")
        
        print("\n" + "="*50)
        print("✓ MySQL is properly configured and connected!")
        print("="*50)
        
except Exception as e:
    print(f"\n✗ Connection failed: {e}")
    print("\nPlease check:")
    print("1. MySQL Server is installed and running")
    print("2. Database 'patient_records_db' exists")
    print("3. Username and password in settings.py are correct")
    print("\nRun these commands in MySQL:")
    print("  CREATE DATABASE patient_records_db CHARACTER SET utf8mb4;")
