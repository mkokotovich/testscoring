from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.testing.models import Test, Item
from apps.testing.serializers import TestSerializer, TestListSerializer, ItemSerializer
from apps.testing.permissions import IsOwnerPermission, IsTestOwnerPermission
from apps.testing.cbcl import CBCL_6_18, CBCL_1_5
from apps.testing.conners import Conners3Parent, Conners3Self
from apps.testing.tscyc import TSCYC
from apps.testing.brief import Brief2
from apps.testing.srs import SRS2
from apps.testing.scared import SCARED
from apps.testing.tscc import TSCC


# Add new assessments to this list
assessments = [
    CBCL_6_18(),
    CBCL_1_5(),
    Conners3Parent(),
    Conners3Self(),
    TSCYC(),
    Brief2(),
    SRS2(),
    SCARED(),
    TSCC(),
]


class TestViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('^client_number',)
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

    def _find_assessment(self, test_type):
        return next((assessment for assessment in assessments
                    if assessment.test_type == test_type),
                    None)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        response = super().create(request)
        assessment = self._find_assessment(response.data['test_type'])
        if not assessment:
            raise APIException(f"Test type {response.data['test_type']} is not supported")
        assessment.create_test(response.data['id'])
        return response

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'types':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsOwnerPermission]

        return super().get_permissions()

    @action(detail=True)
    def scores(self, request, pk=None):
        test = Test.objects.prefetch_related('items').get(id=pk)
        assessment = self._find_assessment(test.test_type)
        if not assessment:
            raise APIException(f"Test type {test.test_type} is not supported")
        scores = assessment.score_test(test)
        return Response(scores)

    @action(detail=False)
    def types(self, request):
        test_types = [{
            'slug': choice[0],
            'name': choice[1],
        } for choice in Test.TEST_TYPE_CHOICES]

        return Response(test_types)


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
