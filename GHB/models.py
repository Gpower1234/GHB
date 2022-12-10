from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Gallery(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='violet/images')

    def __str__(self):
        return self.name