from django.urls import path
from . import views

app_name = 'content_management'

urlpatterns = [
    path('', views.home, name='home'),
]
