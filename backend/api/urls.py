"""testscoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def up(request, format=None):
    data = {
        "status": "happy"
    }
    return Response(data)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^up/$', up),
    url(r'^api/auth/', obtain_jwt_token),
    url(r'^api/users/', include('evaluators.urls')),
    url(r'^api/testing/', include('apps.testing.urls')),
]
