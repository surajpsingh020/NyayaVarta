from rest_framework import serializers
from .models import LegalCategory, LegalContent, ContentTranslation, LegalModule, UserContentInteraction

class LegalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCategory
        fields = '__all__'

class ContentTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTranslation
        fields = '__all__'

class LegalContentSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    translations = ContentTranslationSerializer(many=True, read_only=True)
    
    class Meta:
        model = LegalContent
        fields = '__all__'

class LegalContentListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = LegalContent
        fields = ['id', 'title', 'summary', 'content_type', 'category_name', 
                 'difficulty_level', 'target_audience', 'estimated_read_time', 
                 'views_count', 'likes_count', 'is_featured', 'created_at']

class LegalModuleSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    contents = LegalContentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = LegalModule
        fields = '__all__'

class UserContentInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContentInteraction
        fields = '__all__'
