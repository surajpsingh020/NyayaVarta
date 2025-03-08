from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.lessons_list, name='lessons_list'),
    # You can add more URL patterns here for quiz detail pages, etc.
]
