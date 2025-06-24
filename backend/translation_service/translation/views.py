from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import SupportedLanguage, TranslationRequest
from .serializers import (
    SupportedLanguageSerializer, 
    TranslationRequestSerializer,
    TextTranslationSerializer,
    SpeechToTextSerializer,
    TextToSpeechSerializer
)
from .services import translation_service

class SupportedLanguageListView(generics.ListAPIView):
    queryset = SupportedLanguage.objects.filter(is_active=True)
    serializer_class = SupportedLanguageSerializer

@api_view(['POST'])
def translate_text(request):
    serializer = TextTranslationSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        source_lang = serializer.validated_data['source_language']
        target_lang = serializer.validated_data['target_language']
        user_id = serializer.validated_data.get('user_id')
        
        # Create translation request
        translation_request = TranslationRequest.objects.create(
            user_id=user_id,
            translation_type='text_to_text',
            source_language=source_lang,
            target_language=target_lang,
            source_text=text,
            status='processing'
        )
        
        try:
            # Perform translation
            translated_text = translation_service.translate_text(text, source_lang, target_lang)
            
            # Update request
            translation_request.translated_text = translated_text
            translation_request.status = 'completed'
            translation_request.completed_at = timezone.now()
            translation_request.save()
            
            return Response({
                'id': translation_request.id,
                'translated_text': translated_text,
                'status': 'completed'
            })
        except Exception as e:
            translation_request.status = 'failed'
            translation_request.error_message = str(e)
            translation_request.save()
            
            return Response({
                'error': 'Translation failed',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def speech_to_text(request):
    serializer = SpeechToTextSerializer(data=request.data)
    if serializer.is_valid():
        audio_url = serializer.validated_data['audio_url']
        language = serializer.validated_data['language']
        user_id = serializer.validated_data.get('user_id')
        
        # Create translation request
        translation_request = TranslationRequest.objects.create(
            user_id=user_id,
            translation_type='speech_to_text',
            source_language=language,
            target_language=language,
            audio_input_url=audio_url,
            status='processing'
        )
        
        try:
            # Perform speech to text
            transcribed_text = translation_service.speech_to_text(audio_url, language)
            
            # Update request
            translation_request.translated_text = transcribed_text
            translation_request.status = 'completed'
            translation_request.completed_at = timezone.now()
            translation_request.save()
            
            return Response({
                'id': translation_request.id,
                'transcribed_text': transcribed_text,
                'status': 'completed'
            })
        except Exception as e:
            translation_request.status = 'failed'
            translation_request.error_message = str(e)
            translation_request.save()
            
            return Response({
                'error': 'Speech to text conversion failed',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def text_to_speech(request):
    serializer = TextToSpeechSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        language = serializer.validated_data['language']
        user_id = serializer.validated_data.get('user_id')
        
        # Create translation request
        translation_request = TranslationRequest.objects.create(
            user_id=user_id,
            translation_type='text_to_speech',
            source_language=language,
            target_language=language,
            source_text=text,
            status='processing'
        )
        
        try:
            # Perform text to speech
            audio_url = translation_service.text_to_speech(text, language)
            
            # Update request
            translation_request.audio_output_url = audio_url
            translation_request.status = 'completed'
            translation_request.completed_at = timezone.now()
            translation_request.save()
            
            return Response({
                'id': translation_request.id,
                'audio_url': audio_url,
                'status': 'completed'
            })
        except Exception as e:
            translation_request.status = 'failed'
            translation_request.error_message = str(e)
            translation_request.save()
            
            return Response({
                'error': 'Text to speech conversion failed',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def translation_status(request, request_id):
    try:
        translation_request = TranslationRequest.objects.get(id=request_id)
        serializer = TranslationRequestSerializer(translation_request)
        return Response(serializer.data)
    except TranslationRequest.DoesNotExist:
        return Response({'error': 'Translation request not found'}, status=status.HTTP_404_NOT_FOUND)
