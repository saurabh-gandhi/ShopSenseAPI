from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.ServiceApiHandlers.get_movie_list_handler import handle_request
from movies.models import Movie, Director, Genre


class MovieList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        movies = Movie.objects.all()
        print movies
        if movies.count() > 0:
            return Response(handle_request(movies))
        else:
            return Response("No Entries in the Database",
                            status.HTTP_204_NO_CONTENT)

    def post(self, request):
        data = request.DATA
        try:
            m = Movie()
            m.name = data["name"]
            m.director, created = Director.objects.get_or_create(name=data["director"])
            m.imdb_score = data["imdb_score"]
            m.popularity = data["99popularity"]
            m.save()
            for genre in data["genre"]:
                genre = genre.strip(" ")
                g , created = Genre.objects.get_or_create(name=genre)
            m.genre.add(g)
        except Exception, e:
            print e
        return Response(handle_request([m]))