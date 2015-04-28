from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=128, db_index=True)


class Genre(models.Model):
    name = models.CharField(max_length=128, db_index=True)


class Movie(models.Model):
    popularity = models.FloatField()
    imdb_score = models.FloatField()
    name = models.CharField(max_length=128, unique=True, db_index=True)
    director = models.ForeignKey(Director)
    genre = models.ManyToManyField(Genre)
