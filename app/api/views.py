from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from django.db.models import Count
from django.db.models.expressions import Window, F
from django.db.models.functions.window import Rank

from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer
from .omdb_handler import get_data_from_omdb


class MovieViews(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', )

    def create(self, request, *args, **kwargs):
        title = request.data['title']

        if Movie.objects.filter(title=title).exists():
            return Response('Movie already exists!', status.HTTP_400_BAD_REQUEST)

        movie_data = get_data_from_omdb(title=title)

        if movie_data == status.HTTP_404_NOT_FOUND:
            return Response('Movie does not exists', status.HTTP_400_BAD_REQUEST)

        post_data = {
            'title': movie_data['Title'],
            'year': movie_data['Year'],
            'rated': movie_data['Rated'],
            'released': movie_data['Released'],
            'runtime': movie_data['Runtime'],
            'genre': movie_data['Genre'],
            'director': movie_data['Director'],
            'writer': movie_data['Writer'],
            'actors': movie_data['Actors'],
            'plot': movie_data['Plot'],
            'language': movie_data['Language'],
            'country': movie_data['Country'],
            'awards': movie_data['Awards'],
            'poster': movie_data['Poster'],
            'ratings': movie_data['Ratings'],
            'metascore': movie_data['Metascore'],
            'imdb_rating': movie_data['imdbRating'],
            'imdb_votes': movie_data['imdbVotes'],
            'imdb_id': movie_data['imdbID'],
            'type': movie_data['Type'],
            'dvd': movie_data['DVD'],
            'box_office': movie_data['BoxOffice'],
            'production': movie_data['Production'],
            'website': movie_data['Website'],
            'response': movie_data['Response'],
        }

        serializer = self.serializer_class(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CommentViews(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('movie', )


class TopView(APIView):
    ranking = Window(
        expression=Rank(),
        order_by=F('num_of_comments').desc()
    )

    def get(self, request):
        query = Comment.objects.select_related('movie').values('movie__title').annotate(
            num_of_comments=Count('movie')).annotate(ranking=self.ranking)
        return Response([movie for movie in query])
