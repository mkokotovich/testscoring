from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.testing.models import Test, Item
from apps.testing.serializers import TestSerializer, TestListSerializer, ItemSerializer
from apps.testing.permissions import IsOwnerPermission, IsTestOwnerPermission
from apps.testing.cbcl import (
    create_cbcl_6_18_test_items,
    create_cbcl_1_5_test_items,
    calculate_cbcl_6_18_test_scores,
    calculate_cbcl_1_5_test_scores,
)
from apps.testing.conners import (
    create_conners3_parent_test_items,
    calculate_conners3_parent_test_scores,
)


create_functions = {
    Test.CBCL_6_18: create_cbcl_6_18_test_items,
    Test.CBCL_1_5: create_cbcl_1_5_test_items,
    Test.CONNERS3_PARENT: create_conners3_parent_test_items,
}

score_functions = {
    Test.CBCL_6_18: calculate_cbcl_6_18_test_scores,
    Test.CBCL_1_5: calculate_cbcl_1_5_test_scores,
    Test.CONNERS3_PARENT: calculate_conners3_parent_test_scores,
}


class TestViewSet(viewsets.ModelViewSet):
    filter_fields = ('test_type', 'client_number')

    def get_queryset(self):
        if self.request.user.is_staff:
            return Test.objects.all().order_by('-created_at')
        else:
            return Test.objects.filter(owner=self.request.user).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return TestListSerializer
        else:
            return TestSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        response = super().create(request)
        create_test = create_functions.get(response.data['test_type'], None)
        if not create_test:
            raise APIException(f"Test type {response.data['test_type']} is not supported")
        create_test(response.data['id'])
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

    @action(detail=True)
    def scores(self, request, pk=None):
        test = Test.objects.prefetch_related('items').get(id=pk)
        score_test = score_functions.get(test.test_type, None)
        if not score_test:
            raise APIException(f"Test type {test.test_type} is not supported")
        scores = score_test(test)
        return Response(scores)

    @action(detail=False)
    def types(self, request):
        test_types = [choice[0] for choice in Test.TEST_TYPE_CHOICES]
        response = {
            'types': test_types
        }
        return Response(response)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
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
