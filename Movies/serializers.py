from rest_framework import serializers 
from Movies.models import Movie


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie