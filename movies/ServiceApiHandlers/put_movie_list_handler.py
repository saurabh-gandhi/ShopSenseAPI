from movies.models import Director, Genre , Movie
from movies.utils import reproduceResponse


def handle_request(data, title):
    try:
        movie = Movie.objects.get(name=title)
        movie.name = data["name"]
        movie.director, created = Director.objects.get_or_create(name=
                                                                 data["director"])
        movie.imdb_score = data["imdb_score"]
        movie.popularity = data["99popularity"]
        movie.save()
        print "saved"
        for genre in movie.genre.all():
            movie.genre.remove(genre)
        for genre in data["genre"]:
            genre = genre.strip(" ")
            genre_instance, created = Genre.objects.get_or_create(name=genre)
            movie.genre.add(genre_instance)
    except Exception, e:
        print e
    return reproduceResponse([movie])
