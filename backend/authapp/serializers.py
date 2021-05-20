from rest_framework import serializers
from authapp import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ['username', 'firstName','lastName','age','gender']