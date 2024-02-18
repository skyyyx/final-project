from djoser.serializers import UserCreateSerializer
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import UserAccount
from .models import Recommend


class CustomUserCreateSerializer(UserCreateSerializer):
    uid = serializers.CharField(required=False)

    token = serializers.CharField(source='auth_token.key', read_only=True)

    class Meta:
        model = UserAccount
        fields = '__all__'

        extra_kwargs = {
            'uid': {'write_only': True, 'required': False},
        }


class CustomUserSerializer(UserSerializer):
    token = serializers.CharField(source='auth_token.key', read_only=True)


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
