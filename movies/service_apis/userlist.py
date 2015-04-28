from django.contrib.auth.models import User
from rest_framework import generics ,permissions

from movies.utils.serializers import UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
