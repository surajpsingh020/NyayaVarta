from django.db import models

class SupportedLanguage(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    native_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class TranslationRequest(models.Model):
    TRANSLATION_TYPES = (
        ('text_to_text', 'Text to Text'),
        ('speech_to_text', 'Speech to Text'),
        ('text_to_speech', 'Text to Speech'),
        ('speech_to_speech', 'Speech to Speech'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    user_id = models.IntegerField(blank=True, null=True)
    translation_type = models.CharField(max_length=20, choices=TRANSLATION_TYPES)
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    source_text = models.TextField(blank=True, null=True)
    translated_text = models.TextField(blank=True, null=True)
    audio_input_url = models.URLField(blank=True, null=True)
    audio_output_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Translation {self.id} - {self.source_language} to {self.target_language}"

class TranslationCache(models.Model):
    source_text_hash = models.CharField(max_length=64, unique=True)
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    translated_text = models.TextField()
    usage_count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['source_text_hash', 'source_language', 'target_language']
