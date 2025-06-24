import requests
import hashlib
import json
from django.conf import settings
from .models import TranslationCache, SupportedLanguage

class BhashiniTranslationService:
    def __init__(self):
        self.api_key = settings.BHASHINI_API_KEY
        self.api_url = settings.BHASHINI_API_URL
    
    def get_cache_key(self, text, source_lang, target_lang):
        """Generate cache key for translation"""
        content = f"{text}_{source_lang}_{target_lang}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def get_cached_translation(self, text, source_lang, target_lang):
        """Get translation from cache if available"""
        cache_key = self.get_cache_key(text, source_lang, target_lang)
        try:
            cache_entry = TranslationCache.objects.get(
                source_text_hash=cache_key,
                source_language=source_lang,
                target_language=target_lang
            )
            cache_entry.usage_count += 1
            cache_entry.save()
            return cache_entry.translated_text
        except TranslationCache.DoesNotExist:
            return None
    
    def cache_translation(self, text, source_lang, target_lang, translated_text):
        """Cache translation result"""
        cache_key = self.get_cache_key(text, source_lang, target_lang)
        TranslationCache.objects.update_or_create(
            source_text_hash=cache_key,
            source_language=source_lang,
            target_language=target_lang,
            defaults={'translated_text': translated_text}
        )
    
    def translate_text(self, text, source_lang, target_lang):
        """Translate text using Bhashini API"""
        # Check cache first
        cached_result = self.get_cached_translation(text, source_lang, target_lang)
        if cached_result:
            return cached_result
        
        # Prepare request payload
        payload = {
            "modelId": "ai4bharat/indictrans-v2-all-gpu",
            "task": "translation",
            "input": [
                {
                    "source": text,
                    "target": ""
                }
            ],
            "config": {
                "language": {
                    "sourceLanguage": source_lang,
                    "targetLanguage": target_lang
                }
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            translated_text = result.get('output', [{}])[0].get('target', text)
            
            # Cache the result
            self.cache_translation(text, source_lang, target_lang, translated_text)
            
            return translated_text
        except Exception as e:
            print(f"Translation error: {str(e)}")
            return text  # Return original text if translation fails
    
    def text_to_speech(self, text, language):
        """Convert text to speech using Bhashini API"""
        payload = {
            "modelId": "ai4bharat/indic-tts-coqui-misc-gpu",
            "task": "tts",
            "input": [
                {
                    "source": text
                }
            ],
            "config": {
                "language": {
                    "sourceLanguage": language
                },
                "gender": "female",
                "quality": "medium"
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            audio_url = result.get('output', [{}])[0].get('audio', '')
            
            return audio_url
        except Exception as e:
            print(f"Text-to-speech error: {str(e)}")
            return None
    
    def speech_to_text(self, audio_url, language):
        """Convert speech to text using Bhashini API"""
        payload = {
            "modelId": "ai4bharat/conformer-multilingual-indo_aryan-gpu",
            "task": "asr",
            "input": [
                {
                    "audio": audio_url
                }
            ],
            "config": {
                "language": {
                    "sourceLanguage": language
                }
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            transcribed_text = result.get('output', [{}])[0].get('source', '')
            
            return transcribed_text
        except Exception as e:
            print(f"Speech-to-text error: {str(e)}")
            return None

# Initialize the service
translation_service = BhashiniTranslationService()
