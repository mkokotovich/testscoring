from rest_framework import serializers

from apps.testing.models import Test, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'number', 'description', 'score', 'group', 'groups')


class TestSerializer(serializers.ModelSerializer):
    items = ItemSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'created_at', 'updated_at', 'owner', 'client_number', 'test_type', 'is_archived', 'items')
        read_only_fields = ('owner', 'items')


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'created_at', 'updated_at', 'owner', 'client_number', 'test_type', 'is_archived')
        read_only_fields = ('owner',)
