from rest_framework import serializers

from apps.testing.models import Test, Item
from apps.testing.utils import description_map


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ('owner',)


class ItemSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return description_map.get(obj.number, f"item {obj.number} description")

    class Meta:
        model = Item
        fields = '__all__'
