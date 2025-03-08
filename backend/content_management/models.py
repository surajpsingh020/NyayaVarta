from django.db import models

class LegalArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    language = models.CharField(max_length=10, default='en')  # e.g., 'en', 'hi'
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title