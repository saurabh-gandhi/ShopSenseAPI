from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie, Director
from movies.service_api_handlers.get_movie_list_handler import handle_request
from movies.utils.logger import logger
from movies.utils.handle_response import handle_response


class MovieSearchByDirector(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, director):
        logger.info("GET Search movies with director name %s" % (director))
        try:
            director_instance, created = Director.objects.get_or_create(name=director)
            movies = Movie.objects.filter(director  =director_instance)
            if movies.count() > 0:
                return Response(handle_response(movies))
            else:
                logger.info("No results matching the search query")
                return Response("No Results matching the search query",
                                status.HTTP_204_NO_CONTENT)
        except Exception, e:
            print e
            logger.error(e)
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)
