from rest_framework.routers import DefaultRouter
from .views import NotificationPreferenceViewSet, CardDetailViewSet

router = DefaultRouter()
router.register(r'notification-preferences', NotificationPreferenceViewSet)
router.register(r'card-details', CardDetailViewSet)

urlpatterns = router.urls
