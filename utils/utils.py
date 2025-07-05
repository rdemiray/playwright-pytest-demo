import random
import string

def generate_random_email(domain="example.com", length=8):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"