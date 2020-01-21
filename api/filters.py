import django_filters as filters

from .models.movie import Movie


class ArrayFieldsFilter(filters.FilterSet):
    genre = filters.CharFilter(lookup_expr='icontains')
    director = filters.CharFilter(lookup_expr='icontains')
    writer = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ('year', 'genre', 'director', 'writer')
