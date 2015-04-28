from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie, Director, Genre
from movies.service_api_handlers.get_movie_list_handler import handle_request


from movies.service_api_handlers import\
                        get_movie_list_handler, post_movie_list_handler


class MovieList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        movies = Movie.objects.all()
        print movies
        if movies.count() > 0:
            return get_movie_list_handler.handle_request(movies)
        else:
            return Response("No Entries in the Database",
                            status.HTTP_204_NO_CONTENT)

    def post(self, request):
        data = request.DATA
        return post_movie_list_handler.handle_request(data)