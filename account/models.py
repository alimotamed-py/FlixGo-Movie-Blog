from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)


    class Meta:
        ordering = ['-username']
        indexes = [models.Index(fields=['-username'])]

    def __str__(self):
        return self.username

