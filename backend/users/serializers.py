from djoser.serializers import UserCreateSerializer
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import UserAccount
from .models import Activity


class CustomUserCreateSerializer(UserCreateSerializer):
    uid = serializers.CharField(required=False)

    token = serializers.CharField(source='auth_token.key', read_only=True)

    class Meta:
        model = UserAccount  # Specify the model associated with the serializer
        fields = '__all__'  # Or specify the fields you want to include/exclude

        extra_kwargs = {
            'uid': {'write_only': True, 'required': False},
        }


class CustomUserSerializer(UserSerializer):
    token = serializers.CharField(source='auth_token.key', read_only=True)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
