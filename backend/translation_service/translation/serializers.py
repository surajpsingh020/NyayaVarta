from rest_framework import serializers
from .models import SupportedLanguage, TranslationRequest

class SupportedLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportedLanguage
        fields = '__all__'

class TranslationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationRequest
        fields = '__all__'
        read_only_fields = ('status', 'translated_text', 'audio_output_url', 'error_message', 'completed_at')

class TextTranslationSerializer(serializers.Serializer):
    text = serializers.CharField()
    source_language = serializers.CharField(max_length=10)
    target_language = serializers.CharField(max_length=10)
    user_id = serializers.IntegerField(required=False)

class SpeechToTextSerializer(serializers.Serializer):
    audio_url = serializers.URLField()
    language = serializers.CharField(max_length=10)
    user_id = serializers.IntegerField(required=False)

class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField()
    language = serializers.CharField(max_length=10)
    user_id = serializers.IntegerField(required=False)
