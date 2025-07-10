from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = router.urls
