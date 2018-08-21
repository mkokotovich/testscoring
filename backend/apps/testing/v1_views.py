from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from apps.testing.models import Test, Item
from apps.testing.serializers import TestSerializer, ItemSerializer
from apps.testing.permissions import IsOwnerPermission


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_fields = ('name',)
    ordering = "-created_at"

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerPermission]
        return super().get_permissions()


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
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
