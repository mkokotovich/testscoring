from django.contrib.auth.models import User
from rest_framework import serializers

from scoring.models import Test, Item
from scoring.utils import description_map


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'tests')
        read_only_fields = ('posts',)


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return description_map.get(obj.number, f"item {obj.number} description")

    class Meta:
        model = Item
        fields = '__all__'
