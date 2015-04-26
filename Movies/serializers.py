from rest_framework.serializers import BaseSerializer, ModelSerializer
from Movies.models import Director, Genre, Movie 


def GenreSerializer(ModelSerializer):
    class meta:
        model = Genre
        fields = ('name')


def DirectorSerializer(ModelSerializer):
    class meta:
        model = Director
        fields =('name')


#def MovieSerializer(BaseSerializer):
