from rest_framework import serializers
from .models import LegalModule

class LegalModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalModule
        fields = '__all__'
