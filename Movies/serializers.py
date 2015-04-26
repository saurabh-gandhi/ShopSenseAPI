from rest_framework import serializers 
from django.contrib.auth.models import User


class UserSerializer(serializers.ListSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )