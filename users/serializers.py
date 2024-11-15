from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

def validate_username(self, username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return username
    raise ValidationError('Username already exists')