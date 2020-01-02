from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Comment, Movie
from ..serializers import CommentSerializer


TOP_COMMENTS_URL = reverse('top')


class CommentViewsTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        movies = {'Shrek': 5, 'Finding Nemo': 3, 'Titanic': 3, 'Avatar': 1}

        for title in movies:
            self.movie = Movie.objects.create(title=title)
            for _ in range(movies[title]):
                Comment.objects.create(movie=self.movie, text=f'Comment_{_}')

    def test_ranking_view(self):
        ranking = [
            {
                'movie__title': 'Shrek',
                'num_of_comments': 5,
                'ranking': 1
            },
            {
                'movie__title': 'Titanic',
                'num_of_comments': 3,
                'ranking': 2
            },
            {
                'movie__title': 'Finding Nemo',
                'num_of_comments': 3,
                'ranking': 2
            },
            {
                'movie__title': 'Avatar',
                'num_of_comments': 1,
                'ranking': 4
            }
        ]

        response = self.client.get(TOP_COMMENTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ranking)
