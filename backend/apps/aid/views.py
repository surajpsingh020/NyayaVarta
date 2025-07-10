from rest_framework import viewsets
from .models import LegalAidService, AidRequest
from .serializers import LegalAidServiceSerializer, AidRequestSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LegalAidServiceViewSet(viewsets.ModelViewSet):
    queryset = LegalAidService.objects.all()
    serializer_class = LegalAidServiceSerializer

class AidRequestViewSet(viewsets.ModelViewSet):
    queryset = AidRequest.objects.all()
    serializer_class = AidRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
