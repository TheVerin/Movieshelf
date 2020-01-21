from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api.models.movie import Movie
from api.serializers.movie_serializer import MovieSerializer


class MovieViewsTest(TestCase):

    def setUp(self) -> None:
        self.get_movies = reverse('get')
        self.create_movie = reverse('create')
        self.client = APIClient()

        movies = ('Shrek', 'Avatar', 'Titanic', 'The Godfather')

        for movie in movies:
            Movie.objects.create(title=movie)

    def test_get_all_movies(self):
        response = self.client.get(self.get_movies)
        from_db = Movie.objects.all()
        serializer = MovieSerializer(from_db, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_movie(self):
        payload = {
            'title': 'Interstellar'
        }

        before = Movie.objects.all().count()

        response = self.client.post(self.create_movie, payload)

        after = Movie.objects.all().count()
        from_db = Movie.objects.latest('pk')
        serializer = MovieSerializer(from_db)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(serializer.data['title'], payload['title'])
        self.assertTrue(before, after)

    def test_create_invalid_movie(self):
        payload = {
            'title': ''
        }

        response = self.client.post(self.create_movie, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, 'Movie does not exists')

    def test_movie_already_exists(self):
        payload = {
            'title': 'Avatar'
        }

        response = self.client.post(self.create_movie, payload)

        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data, 'Movie already exists!')
