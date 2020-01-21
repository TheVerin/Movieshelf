from rest_framework import serializers

from api.models.movie import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class JustTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
