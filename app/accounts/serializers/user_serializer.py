from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework.serializers import ModelSerializer, Serializer, ValidationError
from rest_framework import serializers

from accounts.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(Serializer):
    """Serializer which creates a new auth token for user."""
    username = serializers.CharField()
    password = serializers.CharField(
        style = {
            "input_type": "password"
        },
        trim_whitespace = False,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )

        if not user:
            message = _("Unable to authenticate with provided credentials.")
            raise ValidationError(message, code="authorization")

        attrs["user"] = user
        return attrs
