from django.db import models
from users.models import User

class LegalAidService(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    region = models.CharField(max_length=100)
    languages_supported = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

class AidRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(LegalAidService, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
    request_time = models.DateTimeField(auto_now_add=True)
    response_time = models.DateTimeField(null=True, blank=True)
