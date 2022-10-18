from rest_framework import routers

from evaluators import v1_views


router = routers.DefaultRouter()
router.register(r'', v1_views.UserViewSet, basename='evaluators')

urlpatterns = router.urls
