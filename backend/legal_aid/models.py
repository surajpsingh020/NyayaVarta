from django.db import models

class LegalAidService(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    language_supported = models.CharField(max_length=10, default='en')
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
