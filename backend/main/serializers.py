from rest_framework import serializers
from main import models
from authapp.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    username = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = models.Post

class CommentSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    class Meta:
        fields = ['description','username']
        model = models.Comment


class LikeSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    class Meta:
        fields = ['username']
        model = models.Comment

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Friends