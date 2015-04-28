from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie, Genre
from movies.service_api_handlers.get_movie_list_handler import handle_request
from movies.utils.logger import logger


class MovieSearchByGenre(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, genre):
        try:
            logger.info("GET Search movies with Genre name %s" % (genre))
            genre_instance, created = Genre.objects.get_or_create(name=genre)
            movies = Movie.objects.filter(genre=genre_instance)
            if movies.count() > 0:
                return Response(handle_request(movies))
            else:
                logger.info("No results matching the search query")
                return Response("No Results matching the search query",
                                status.HTTP_204_NO_CONTENT)
        except Exception, e:
            logger.error(e)
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)
