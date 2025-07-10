from rest_framework.routers import DefaultRouter
from .views import LegalModuleViewSet

router = DefaultRouter()
router.register(r'modules', LegalModuleViewSet)

urlpatterns = router.urls
