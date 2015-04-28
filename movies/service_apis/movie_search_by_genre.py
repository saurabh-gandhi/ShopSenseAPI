from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.ServiceApiHandlers.get_movie_list_handler import handle_request
from movies.models import Movie, Genre


class MovieSearchByGenre(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, genre):
        movies = Movie.objects.filter(genre=Genre.objects.get(name=genre))
        if movies.count() > 0:
            return Response(handle_request(movies))
        else:
            return Response("No Entry found",
                            status.HTTP_204_NO_CONTENT)
