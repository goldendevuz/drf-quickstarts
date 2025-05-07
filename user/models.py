from django.contrib.auth.models import AbstractUser
from django.db import models

def hash_file_name(instance, filename):
    # Generate a unique file name using the original file name and a hash
    import hashlib, os
    hashed_filename = hashlib.sha256(filename.encode('utf-8')).hexdigest()

    # Get the file extension
    ext = os.path.splitext(filename)[1]

    # Return the new file name
    return f"profile_pics/{hashed_filename}{ext}"

class User(AbstractUser):
    image = models.ImageField(upload_to=hash_file_name, null=True, blank=True)
