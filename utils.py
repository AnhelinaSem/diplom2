import uuid
import random
import string

def create_unique_email():
    unique_id = uuid.uuid4()
    return f"user_{unique_id}@example.com"

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
