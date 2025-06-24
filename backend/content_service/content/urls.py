from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.LegalCategoryListView.as_view(), name='legal_categories'),
    path('contents/', views.LegalContentListView.as_view(), name='legal_contents'),
    path('contents/<int:pk>/', views.LegalContentDetailView.as_view(), name='legal_content_detail'),
    path('contents/featured/', views.FeaturedContentView.as_view(), name='featured_content'),
    path('modules/', views.LegalModuleListView.as_view(), name='legal_modules'),
    path('modules/<int:pk>/', views.LegalModuleDetailView.as_view(), name='legal_module_detail'),
    path('interaction/', views.content_interaction, name='content_interaction'),
    path('search/', views.search_content, name='search_content'),
]
