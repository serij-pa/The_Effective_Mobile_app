from django.contrib.auth.models import Group, User
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("pk",
                  "name",
                  "user_set", "permissions")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "pk", "username", "is_active", 'groups', "user_permissions",
