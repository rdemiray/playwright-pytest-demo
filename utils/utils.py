import random
import string

def generate_random_email(domain="gmail.com", length=8):
    """Generate a random email address with a given domain."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"

def generate_password(length=5):
    """Generate a random password with letters and digits."""
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    password = ''.join(random.choices(characters, k=length))
    return password