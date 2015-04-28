from rest_framework import status
from movies.models import Movie
from rest_framework.response import Response


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
            print movie_list
        return Response(movie_list)
    except Exception , e:
        print e