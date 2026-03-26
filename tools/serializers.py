from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Category, Tools, FeedBack

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = Category

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = Tools

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = FeedBack

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'