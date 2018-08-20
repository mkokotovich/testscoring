from rest_framework import routers

from apps.testing import v1_views


router = routers.DefaultRouter()
router.register(r'tests', v1_views.TestViewSet, base_name='tests')
router.register(r'items', v1_views.ItemViewSet, base_name='items')

urlpatterns = router.urls
