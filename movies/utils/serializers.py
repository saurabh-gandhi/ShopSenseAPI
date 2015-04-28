from rest_framework import serializers 
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        print "here"
        model = User
        fields = ["id",'username']