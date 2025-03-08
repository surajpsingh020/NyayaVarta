from django.urls import path
from . import views

app_name = 'legal_aid'

urlpatterns = [
    path('', views.service_list, name='service_list'),
]
