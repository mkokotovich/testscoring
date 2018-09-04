from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from apps.user.serializers import UserSerializer
from apps.user.permissions import IsOwnerPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    ordering = "-date_joined"

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsOwnerPermission, ]
        return super(UserViewSet, self).get_permissions()
