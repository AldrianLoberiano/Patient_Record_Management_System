"""
Interactive MySQL Password Tester
Helps you find the correct MySQL password for your Django settings
"""

import getpass

def test_mysql_connection(password):
    """Test MySQL connection with given password"""
    try:
        import MySQLdb
        
        conn = MySQLdb.connect(
            host='localhost',
            user='root',
            password=password,
            port=3306
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        
        print(f"\n✓ SUCCESS! Connection established!")
        print(f"✓ MySQL Version: {version[0]}")
        
        # Try to access the database
        cursor.execute("SHOW DATABASES LIKE 'patient_records_db'")
        result = cursor.fetchone()
        
        if result:
            print(f"✓ Database 'patient_records_db' exists!")
        else:
            print(f"\n⚠ Database 'patient_records_db' does NOT exist yet.")
            print(f"  Run this command to create it:")
            create_cmd = input("\nWould you like to create it now? (yes/no): ")
            
            if create_cmd.lower() in ['yes', 'y']:
                cursor.execute("CREATE DATABASE patient_records_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
                print("✓ Database created successfully!")
        
        conn.close()
        
        print("\n" + "="*60)
        print("Update your settings.py with:")
        print("="*60)
        print(f"'USER': 'root',")
        print(f"'PASSWORD': '{password}',")
        print("="*60)
        
        return True
        
    except MySQLdb.OperationalError as e:
        if "Access denied" in str(e):
            print(f"\n✗ Wrong password. Try again.")
            return False
        elif "Can't connect" in str(e):
            print(f"\n✗ MySQL Server is not running or not installed.")
            print(f"  Please start MySQL service or install MySQL Server.")
            return None
        else:
            print(f"\n✗ Error: {e}")
            return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False

def main():
    print("="*60)
    print("MySQL Password Finder for Django")
    print("="*60)
    print("\nThis will help you find the correct MySQL root password.")
    print("Press Ctrl+C to exit at any time.\n")
    
    # Common passwords to try
    common_passwords = ['', 'root', 'password', 'admin', 'mysql']
    
    print("Trying common passwords first...\n")
    for pwd in common_passwords:
        pwd_display = "''" if pwd == '' else pwd
        print(f"Trying: {pwd_display}...", end=" ")
        result = test_mysql_connection(pwd)
        if result:
            return
        elif result is None:
            return
    
    print("\n" + "-"*60)
    print("Common passwords didn't work. Let's try manually.")
    print("-"*60)
    
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            password = getpass.getpass(f"\nEnter MySQL root password (attempt {attempts + 1}/{max_attempts}): ")
            
            result = test_mysql_connection(password)
            if result:
                return
            elif result is None:
                return
                
            attempts += 1
            
        except KeyboardInterrupt:
            print("\n\nExiting...")
            return
    
    print("\n" + "="*60)
    print("Maximum attempts reached.")
    print("="*60)
    print("\nIf you've forgotten your password, see:")
    print("  MYSQL_PASSWORD_RESET.md")
    print("\nOr temporarily switch back to SQLite in settings.py")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
