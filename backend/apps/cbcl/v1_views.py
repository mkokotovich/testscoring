from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from apps.cbcl.models import CBCLTest, CBCLItem
from apps.cbcl.serializers import CBCLTestSerializer, CBCLItemSerializer
from apps.cbcl.permissions import IsOwnerPermission


class CBCLTestViewSet(viewsets.ModelViewSet):
    queryset = CBCLTest.objects.all()
    serializer_class = CBCLTestSerializer
    filter_fields = ('name',)
    ordering = "-created_at"

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerPermission]
        return super().get_permissions()


class CBCLItemViewSet(viewsets.ModelViewSet):
    queryset = CBCLItem.objects.all()
    serializer_class = CBCLItemSerializer
    filter_fields = ('name',)
    ordering = "-number"

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerPermission]
        return super().get_permissions()
