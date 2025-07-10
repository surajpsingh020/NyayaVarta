from rest_framework import serializers
from .models import LegalAidService, AidRequest

class LegalAidServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalAidService
        fields = '__all__'

class AidRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidRequest
        fields = '__all__'
