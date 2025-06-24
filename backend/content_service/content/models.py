from django.db import models

class LegalCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Legal Categories"
    
    def __str__(self):
        return self.name

class LegalContent(models.Model):
    CONTENT_TYPES = (
        ('article', 'Article'),
        ('guide', 'Guide'),
        ('faq', 'FAQ'),
        ('case_study', 'Case Study'),
        ('law_summary', 'Law Summary'),
    )
    
    DIFFICULTY_LEVELS = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    
    TARGET_AUDIENCES = (
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('senior_citizen', 'Senior Citizen'),
        ('general', 'General Public'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    category = models.ForeignKey(LegalCategory, on_delete=models.CASCADE, related_name='contents')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='beginner')
    target_audience = models.CharField(max_length=20, choices=TARGET_AUDIENCES, default='general')
    tags = models.JSONField(default=list)
    language = models.CharField(max_length=10, default='en')
    estimated_read_time = models.IntegerField(default=5)  # in minutes
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class ContentTranslation(models.Model):
    content = models.ForeignKey(LegalContent, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    translated_content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['content', 'language']
    
    def __str__(self):
        return f"{self.content.title} - {self.language}"

class LegalModule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(LegalCategory, on_delete=models.CASCADE, related_name='modules')
    contents = models.ManyToManyField(LegalContent, related_name='modules')
    order = models.IntegerField(default=0)
    estimated_duration = models.IntegerField(default=30)  # in minutes
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class UserContentInteraction(models.Model):
    INTERACTION_TYPES = (
        ('view', 'View'),
        ('like', 'Like'),
        ('bookmark', 'Bookmark'),
        ('share', 'Share'),
        ('complete', 'Complete'),
    )
    
    user_id = models.IntegerField()  # Reference to user from auth service
    content = models.ForeignKey(LegalContent, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user_id', 'content', 'interaction_type']
