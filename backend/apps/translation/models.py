from django.db import models

class Translation(models.Model):
    source_text = models.TextField()
    translated_text = models.TextField()
    source_lang = models.CharField(max_length=10)
    target_lang = models.CharField(max_length=10)
    type = models.CharField(max_length=10)  # tts, stt, ttt, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
