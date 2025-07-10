from rest_framework.routers import DefaultRouter
from .views import LegalAidServiceViewSet, AidRequestViewSet

router = DefaultRouter()
router.register(r'services', LegalAidServiceViewSet)
router.register(r'requests', AidRequestViewSet)

urlpatterns = router.urls
