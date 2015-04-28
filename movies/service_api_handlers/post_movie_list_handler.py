from rest_framework.response import Response

from movies.models import Movie, Director, Genre
from movies.utils.handle_response import handle_response
from rest_framework import status


def handle_request(data):
    try:
        movie, created = Movie.objects.get_or_create(name=data["name"])
        if not created:
            return Response("Movie Already Exists",
                            status.HTTP_400_BAD_REQUEST) 
        movie.director, created = Director.objects.get_or_create(name=data["director"])
        movie.imdb_score = data["imdb_score"]
        movie.popularity = data["99popularity"]
        movie.save()
        try:
            for genre in data["genre"]:
                genre = genre.strip(" ")
                genre_instance, created = Genre.objects.get_or_create(name=genre)
                movie.genre.add(genre_instance)
        except Exception:
            movie.delete()
            return Response("Missing parameter genre", status.HTTP_400_BAD_REQUEST)
        return Response(handle_response([movie]))
    except Exception, e:
        return Response("Bad request", status.HTTP_400_BAD_REQUEST)
