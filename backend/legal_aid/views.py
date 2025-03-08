from django.shortcuts import render
from .models import LegalAidService

def service_list(request):
    services = LegalAidService.objects.all()
    return render(request, 'legal_aid/service_list.html', {'services': services})
