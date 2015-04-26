from django.db import models


class Director(models.Model):
    name = models.TextField()


class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    popularity = models.FloatField()
    imdb_score = models.FloatField()
    name = models.TextField(unique=True)
    director = models.ForeignKey(Director)
    genre = models.ManyToManyField(Genre)
