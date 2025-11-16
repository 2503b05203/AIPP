import hashlib
import getpass

# Store hashed passwords (in production, use a database)
USERS = {
    "john": hashlib.sha256("secure_password_123".encode()).hexdigest(),
    "alice": hashlib.sha256("my_secure_pass".encode()).hexdigest(),
}

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    """Authenticate user with username and password"""
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ")
        
        if username in USERS and USERS[username] == hash_password(password):
            print(f"Welcome, {username}!")
            return True
        
        attempts += 1
        print(f"Invalid credentials. Attempts remaining: {max_attempts - attempts}")
    
    print("Login failed. Too many attempts.")
    return False

if __name__ == "__main__":
    login()

    