from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = (
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('senior', 'Senior Citizen'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=USER_ROLES)
    language_preference = models.CharField(max_length=10, default='en')
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
