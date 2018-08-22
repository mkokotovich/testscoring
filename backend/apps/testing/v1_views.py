from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from apps.testing.models import Test, Item
from apps.testing.serializers import TestSerializer, ItemSerializer
from apps.testing.permissions import IsOwnerPermission
from apps.testing.cbcl import create_cbcl_6_18_test_items


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_fields = ('name', 'test_type')
    ordering = "-created_at"

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        response = super().create(request)
        if response.data['test_type'] == Test.CBCL_6_18:
            create_cbcl_6_18_test_items(response.data['id'])
        return response

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
