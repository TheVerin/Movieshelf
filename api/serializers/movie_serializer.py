from rest_framework import serializers

from api.models.movie import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'year', 'rated', 'released', 'runtime', 'genre', 'director', 'writer',
                  'actors', 'plot', 'language', 'country', 'awards', 'poster', 'ratings',
                  'metascore', 'imdb_rating', 'imdb_votes', 'imdb_id', 'type', 'dvd', 'box_office',
                  'production', 'website')


class JustTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
