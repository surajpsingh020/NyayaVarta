from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (('student', 'Student'), ('professional', 'Professional'), ('senior', 'Senior Citizen'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    language_pref = models.CharField(max_length=10, default='en')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    occupation = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
