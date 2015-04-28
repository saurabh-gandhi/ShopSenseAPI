from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.service_api_handlers import \
    get_movie_list_handler, put_movie_edit_handler
from movies.utils.logger import logger


class MovieSearchByTitle(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, title):
        logger.info("GET Search movies with title %s" % (title))
        movies = Movie.objects.filter(name=title)
        if movies:
            return Response(get_movie_list_handler.handle_request(movies))
        else:
            return Response("No Entry found",
                            status.HTTP_204_NO_CONTENT)

    def put(self, request, title):
        data = request.DATA
        logger.info("PUT Edit movie with title %s" % (title))
        put_movie_edit_handler.handle_request(data, title)

    def delete(self, request, title):
        logger.info("DELETE delete movie with title %s" % (title))
        movie = Movie.objects.filter(name=title)
        movie.delete()