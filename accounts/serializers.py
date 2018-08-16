from django.contrib.auth import get_user_model
from .models import UserProfile
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    CharField
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        username = data['username']
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError('Username already exists!')
        return data
    
    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'organisation',
            'defaultSite',
            'color',
        ]

class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile',
        ]

class UserOnlySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]