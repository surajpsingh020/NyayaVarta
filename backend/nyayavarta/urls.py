from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/content/', include('content.urls')),
    path('api/translation/', include('translation.urls')),
    path('api/aid/', include('aid.urls')),
    path('api/notifications/', include('notifications.urls')),
]
