from rest_framework.views import APIView
from rest_framework.response import Response
from Movies.models import Movie
from Movies.serializers import MovieSerializer


class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
