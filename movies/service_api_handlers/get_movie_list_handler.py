from rest_framework import status
from rest_framework.response import Response

from movies.models import Movie
from movies.utils.logger import logger


def handle_request(movies):
    try:
        movie_list = []
        for movie in movies:
            each_movie = {}
            each_movie["name"] = movie.name
            each_movie["director"] = movie.director.name
            each_movie["imdb_score"] = movie.imdb_score
            each_movie["99popularity"] = movie.popularity
            genre_list = []
            print each_movie
            for genre in movie.genre.all():
                genre_list.append(genre.name)
            each_movie["genre"] = genre_list
            movie_list.append(each_movie)
        logger.info("Displaying the list of Movies")
        return Response(movie_list)
    except Exception, e:
        logger.info("Caught exception while GET movie List")
        logger.error(e)