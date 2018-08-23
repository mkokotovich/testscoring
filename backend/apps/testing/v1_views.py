from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from apps.testing.models import Test, Item
from apps.testing.serializers import TestSerializer, TestListSerializer, ItemSerializer
from apps.testing.permissions import IsOwnerPermission, IsTestOwnerPermission
from apps.testing.cbcl import create_cbcl_6_18_test_items


class TestViewSet(viewsets.ModelViewSet):
    filter_fields = ('name', 'test_type')
    ordering = "-created_at"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Test.objects.all()
        else:
            return Test.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TestListSerializer
        else:
            return TestSerializer

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
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsOwnerPermission]
        return super().get_permissions()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    filter_fields = ('name',)
    ordering = "-number"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Item.objects.all()
        else:
            return Item.objects.filter(test__owner=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsTestOwnerPermission]
        return super().get_permissions()
