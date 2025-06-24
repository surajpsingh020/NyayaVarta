from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('senior_citizen', 'Senior Citizen'),
        ('general', 'General Public'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='general')
    preferred_language = models.CharField(max_length=10, default='en')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    learning_progress = models.JSONField(default=dict)
    quiz_scores = models.JSONField(default=dict)
    certificates = models.JSONField(default=list)
    bookmarks = models.JSONField(default=list)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
