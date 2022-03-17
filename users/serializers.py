from rest_framework import serializers
from .models import UserAccount

class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = UserAccount
        fields = ('username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name')

class UserScoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'score')