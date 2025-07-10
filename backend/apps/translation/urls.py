from rest_framework.routers import DefaultRouter
from .views import TranslationViewSet

router = DefaultRouter()
router.register(r'', TranslationViewSet)

urlpatterns = router.urls
