from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length = 255)
    last_name = serializers.CharField(max_length = 255)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        return user
