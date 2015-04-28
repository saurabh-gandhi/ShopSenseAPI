from rest_framework import status

from movies.models import Director, Genre, Movie
from movies.utils import handle_response
from movies.utils.logger import logger


def handle_request(data, title):
    try:
        movie = Movie.objects.get(name=title)
        movie.name = data["name"]
        movie.director, created = Director.objects.get_or_create(name=
                                                                 data["director"])
        movie.imdb_score = data["imdb_score"]
        movie.popularity = data["99popularity"]
        movie.save()
        for genre in movie.genre.all():
            movie.genre.remove(genre)
        for genre in data["genre"]:
            genre = genre.strip(" ")
            genre_instance, created = Genre.objects.get_or_create(name=genre)
            movie.genre.add(genre_instance)
    except Exception, e:
        logger.error(e)
        return {"Bad Request", status.HTTP_400_BAD_REQUEST}
    return handle_response([movie])
