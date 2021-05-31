from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
