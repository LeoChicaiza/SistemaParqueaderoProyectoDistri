
# Simulación de base de datos de usuarios
user_passwords = {}

def init():
    global user_passwords
    user_passwords = {
        "admin@example.com": "admin123",
        "user@example.com": "userpass"
    }
