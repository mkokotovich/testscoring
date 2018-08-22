from rest_framework import serializers

from apps.testing.models import Test, Item
from apps.testing.utils import description_map


class ItemSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return description_map.get(obj.number, f"item {obj.number} description")

    class Meta:
        model = Item
        fields = '__all__'


class ItemSummarySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return description_map.get(obj.number, f"item {obj.number} description")

    class Meta:
        model = Item
        fields = ('number','description','score')


class TestSerializer(serializers.ModelSerializer):
    items = ItemSummarySerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ('owner', 'items')


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ('owner',)
