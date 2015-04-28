from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.serializers import UserSerializer
from movies.models import Movie, Director, Genre
from movies.ServiceApiHandlers.get_movie_list_handler import handle_request


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieView(APIView):
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


class MovieSearchByDirector(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, director):
        movies = Movie.objects.filter(director=
                                      Director.objects.get(name=director))
        if movies.count() > 0:
            return Response(handle_request(movies))
        else:
            return Response("No Entry found",
                            status.HTTP_204_NO_CONTENT)


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


class MovieSearchByGenre(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, genre):
        movies = Movie.objects.filter(genre=Genre.objects.get(name=genre))
        if movies.count() > 0:
            return Response(handle_request(movies))
        else:
            return Response("No Entry found",
                            status.HTTP_204_NO_CONTENT)
