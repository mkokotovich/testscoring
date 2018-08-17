from rest_framework import routers

from scoring import v1_views


router = routers.DefaultRouter()
router.register(r'users', v1_views.UserViewSet, base_name='users')
router.register(r'tests', v1_views.TestViewSet, base_name='tests')
router.register(r'items', v1_views.ItemViewSet, base_name='items')

urlpatterns = router.urls
