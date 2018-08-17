from rest_framework import routers

from apps.cbcl import v1_views


router = routers.DefaultRouter()
router.register(r'tests', v1_views.CBCLTestViewSet, base_name='tests')
router.register(r'items', v1_views.CBCLItemViewSet, base_name='items')

urlpatterns = router.urls
