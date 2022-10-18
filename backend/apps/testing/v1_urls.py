from rest_framework import routers

from apps.testing import v1_views


router = routers.DefaultRouter()
router.register(r'tests', v1_views.TestViewSet, basename='tests')
router.register(r'items', v1_views.ItemViewSet, basename='items')

urlpatterns = router.urls
