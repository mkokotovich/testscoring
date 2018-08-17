from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User

from scoring.models import Test, Item
from scoring.serializers import UserSerializer, TestSerializer, ItemSerializer
from scoring.permissions import IsOwnerPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(UserViewSet, self).get_permissions()


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
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
