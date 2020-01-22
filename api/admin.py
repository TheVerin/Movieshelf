from django.contrib import admin

from .models.movie import Movie
from .models.comment import Comment

admin.site.register(Movie, Comment)
