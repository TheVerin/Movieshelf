import json

from django.test import TestCase

from rest_framework import status

from api.tools.omdb_handler import OMDBHandler


class OMDBAPITest(TestCase):
    handler = OMDBHandler()

    def test_get_valid_movie(self):
        with open('api/tests/example_omdb_response.json', 'r') as json_file:
            data = json.loads(json_file.read())
            movie = self.handler.get_data_from_omdb('shrek')
            self.assertEqual(data, movie)

    def test_invalid_movie(self):
        movie = self.handler.get_data_from_omdb('IBetThereIsNoMovieLikeThat')
        self.assertEqual(movie, status.HTTP_404_NOT_FOUND)
