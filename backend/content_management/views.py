from django.shortcuts import render
from .models import LegalArticle

def home(request):
    articles = LegalArticle.objects.all().order_by('-published_date')
    return render(request, 'content_management/home.html', {'articles': articles})
