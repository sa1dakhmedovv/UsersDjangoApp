from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)

    def __str__(self):
        return f'Profile {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=140, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name or self.user.username



