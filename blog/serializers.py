from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Post

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'author', 'created_date', 'updated_date', 'image']
        read_only_fields = ['author', 'slug', 'created_date', 'updated_date']