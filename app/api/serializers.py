from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class OnlyTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
