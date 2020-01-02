import django_filters as filters

from .models import Movie


class ArrayFieldsFilter(filters.FilterSet):
    genre = filters.CharFilter(lookup_expr='icontains')
    director = filters.CharFilter(lookup_expr='icontains')
    writers = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ('year', 'genre', 'director', 'writer')
