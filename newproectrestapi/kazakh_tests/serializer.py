from rest_framework import serializers
from .models import User, KazakhTest  # Импортируйте модели


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Укажите конкретные поля, если нужно


class KazakhTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = KazakhTest
        fields = '__all__'  # Укажите конкретные поля, если нужно
