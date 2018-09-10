from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from apps.user.serializers import UserSerializer, ChangePasswordSerializer
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

    @action(detail=False, methods=['post'])
    def changepassword(self, request):
        user = self.request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(serializer.data['old_password']):
            return Response({"old_password", "Unable to verify current password"},
                            status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.data['new_password'])
        user.save()
        return Response({'status': 'password set'})
