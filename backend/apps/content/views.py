from rest_framework import viewsets
from .models import LegalModule
from .serializers import LegalModuleSerializer

class LegalModuleViewSet(viewsets.ModelViewSet):
    queryset = LegalModule.objects.all()
    serializer_class = LegalModuleSerializer
