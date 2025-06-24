from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import LegalCategory, LegalContent, LegalModule, UserContentInteraction
from .serializers import (
    LegalCategorySerializer, 
    LegalContentSerializer, 
    LegalContentListSerializer,
    LegalModuleSerializer,
    UserContentInteractionSerializer
)

class LegalCategoryListView(generics.ListAPIView):
    queryset = LegalCategory.objects.all()
    serializer_class = LegalCategorySerializer

class LegalContentListView(generics.ListAPIView):
    queryset = LegalContent.objects.filter(is_published=True)
    serializer_class = LegalContentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'content_type', 'difficulty_level', 'target_audience', 'language']
    search_fields = ['title', 'content', 'tags']
    ordering_fields = ['created_at', 'views_count', 'likes_count']
    ordering = ['-created_at']

class LegalContentDetailView(generics.RetrieveAPIView):
    queryset = LegalContent.objects.filter(is_published=True)
    serializer_class = LegalContentSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment view count
        instance.views_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class FeaturedContentView(generics.ListAPIView):
    queryset = LegalContent.objects.filter(is_published=True, is_featured=True)
    serializer_class = LegalContentListSerializer

class LegalModuleListView(generics.ListAPIView):
    queryset = LegalModule.objects.filter(is_published=True)
    serializer_class = LegalModuleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

class LegalModuleDetailView(generics.RetrieveAPIView):
    queryset = LegalModule.objects.filter(is_published=True)
    serializer_class = LegalModuleSerializer

@api_view(['POST'])
def content_interaction(request):
    serializer = UserContentInteractionSerializer(data=request.data)
    if serializer.is_valid():
        interaction = serializer.save()
        
        # Update content statistics
        content = interaction.content
        if interaction.interaction_type == 'like':
            content.likes_count += 1
            content.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_content(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    target_audience = request.GET.get('target_audience', '')
    
    contents = LegalContent.objects.filter(is_published=True)
    
    if query:
        contents = contents.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        )
    
    if category:
        contents = contents.filter(category__name__icontains=category)
    
    if target_audience:
        contents = contents.filter(target_audience=target_audience)
    
    serializer = LegalContentListSerializer(contents, many=True)
    return Response(serializer.data)
