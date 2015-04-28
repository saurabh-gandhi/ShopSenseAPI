from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.service_api_handlers.get_movie_list_handler import handle_request
from movies.models import Movie, Director


class MovieSearchByDirector(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, director):
        try:
            director_instance, created = Director.objects.get_or_create(name=director)
            movies = Movie.objects.filter(genre=director_instance)
            if movies.count() > 0:
                return Response(handle_request(movies))
            else:
                return Response("No Entry found",
                                status.HTTP_204_NO_CONTENT)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)
