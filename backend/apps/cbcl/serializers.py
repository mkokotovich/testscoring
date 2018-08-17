from rest_framework import serializers

from apps.cbcl.models import CBCLTest, CBCLItem
from apps.cbcl.utils import description_map


class CBCLTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBCLTest
        fields = '__all__'


class CBCLItemSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return description_map.get(obj.number, f"item {obj.number} description")

    class Meta:
        model = CBCLItem
        fields = '__all__'
