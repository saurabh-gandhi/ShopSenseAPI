from django.contrib.auth.models import User
from rest_framework import generics

from movies.utils.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
