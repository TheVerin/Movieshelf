from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField(blank=True, null=True)
    rated = models.CharField(max_length=255, blank=True, null=True)
    released = models.DateField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    genre = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    director = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    writer = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    actors = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    awards = models.CharField(max_length=255, blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)
    ratings = ArrayField(
        ArrayField(models.CharField(max_length=255), blank=True, null=True), blank=True, null=True)
    metascore = models.IntegerField(blank=True, null=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    imdb_votes = models.IntegerField(blank=True, null=True)
    imdb_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    dvd = models.DateField(blank=True, null=True)
    box_office = models.IntegerField(blank=True, null=True)
    production = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    response = models.BooleanField(blank=True, null=True)


class Comment(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
