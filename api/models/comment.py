from django.db import models

from .movie import Movie


class Comment(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
