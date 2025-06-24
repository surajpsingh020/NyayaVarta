from django.urls import path
from . import views

urlpatterns = [
    path('languages/', views.SupportedLanguageListView.as_view(), name='supported_languages'),
    path('translate/', views.translate_text, name='translate_text'),
    path('speech-to-text/', views.speech_to_text, name='speech_to_text'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
    path('status/<int:request_id>/', views.translation_status, name='translation_status'),
]
