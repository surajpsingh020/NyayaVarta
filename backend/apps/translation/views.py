from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Translation
from .serializers import TranslationSerializer
import os
import requests

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        source_text = data.get('source_text')
        source_lang = data.get('source_lang')
        target_lang = data.get('target_lang')
        type_ = data.get('type')

        translated_text = f"Translated({source_text})"  

        translation = Translation.objects.create(
            source_text=source_text,
            translated_text=translated_text,
            source_lang=source_lang,
            target_lang=target_lang,
            type=type_
        )
        serializer = self.get_serializer(translation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
