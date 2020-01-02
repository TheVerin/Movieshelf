from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Comment, Movie
from ..serializers import CommentSerializer


ALL_COMMENTS_URL = reverse('comment')


class CommentViewsTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.movie = Movie.objects.create(title='Shrek')

        for _ in range(3):
            Comment.objects.create(movie=self.movie, text=f'Comment_{_}')

    def test_get_all_comments(self):
        response = self.client.get(ALL_COMMENTS_URL)
        from_db = Comment.objects.all()
        serializer = CommentSerializer(from_db, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_create_valid_comment(self):
        payload = {
            'movie': self.movie.pk,
            'text': 'Completely new comment'
        }

        before = Comment.objects.all().count()

        response = self.client.post(ALL_COMMENTS_URL, payload)

        after = Comment.objects.all().count()
        from_db = Comment.objects.latest('pk')
        serializer = CommentSerializer(from_db)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(serializer.data['text'], payload['text'])
        self.assertTrue(before, after)

    def test_create_no_text_comment(self):
        payload = {
            'movie': self.movie.pk,
            'text': ''
        }

        response = self.client.post(ALL_COMMENTS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
