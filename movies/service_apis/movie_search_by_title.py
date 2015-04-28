from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.ServiceApiHandlers.get_movie_list_handler import handle_request
from movies.models import Movie, Director, Genre


class MovieSearchByTitle(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, title):
        movies = Movie.objects.filter(name=title)
        if movies:
            return Response(handle_request(movies))
        else:
            return Response("No Entry found",
                            status.HTTP_204_NO_CONTENT)

    def put(self, request, title):
        data = request.DATA
        print data
        try:
            m = Movie.objects.get(name=title)
            m.name = data["name"]
            m.director, created = Director.objects.get_or_create(name=
                                                                 data["director"])
            m.imdb_score = data["imdb_score"]
            m.popularity = data["99popularity"]
            m.save()
            print "saved"
            for genre in m.genre.all():
                m.genre.remove(genre)
            for genre in data["genre"]:
                genre = genre.strip(" ")
                g, created = Genre.objects.get_or_create(name=genre)
                m.genre.add(g)
        except Exception, e:
            print e
        return Response(handle_request([m]))


    def delete(self, request, title):

        movie = Movie.objects.filter(name=title)
        movie.delete()