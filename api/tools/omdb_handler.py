import json
import requests
from datetime import datetime

from rest_framework.status import HTTP_404_NOT_FOUND

from django.conf import settings


class OMDBHandler:

    @staticmethod
    def get_data_from_omdb(title):
        payload = {'t': title, 'apikey': settings.OMBDAPI_KEY}
        movie_data = json.loads(requests.get('http://www.omdbapi.com/', params=payload).text)
        if 'Error' not in movie_data.keys():
            movie_data['Year'] = int(movie_data['Year']) if movie_data['Year'] != 'N/A' else None

            movie_data['Runtime'] = int(movie_data['Runtime'].split()[0]) \
                if movie_data['Runtime'] != 'N/A' else None

            movie_data['Released'] = str(datetime.strptime(movie_data['Released'],
                                                           '%d %b %Y').date()) \
                if movie_data['Released'] != 'N/A' else None

            movie_data['Genre'] = movie_data['Genre'].split(', ') \
                if movie_data['Genre'] != 'N/A' else 'N/A'

            movie_data['Director'] = movie_data['Director'].split(', ') \
                if movie_data['BoxOffice'] != 'N/A' else None

            movie_data['Writer'] = movie_data['Writer'].split(', ') \
                if movie_data['Writer'] != 'N/A' else None

            movie_data['Actors'] = movie_data['Actors'].split(', ') \
                if movie_data['Actors'] != 'N/A' else None

            movie_data['Ratings'] = [[rating['Source'], rating['Value']]
                                     for rating in movie_data['Ratings']] \
                if movie_data['Ratings'] != 'N/A' else None

            movie_data['Metascore'] = int(movie_data['Metascore']) \
                if movie_data['Metascore'] != 'N/A' else None

            movie_data['imdbRating'] = float(movie_data['imdbRating']) \
                if movie_data['imdbRating'] != 'N/A' else None

            movie_data['imdbVotes'] = int(''.join(movie_data['imdbVotes'].split(','))) \
                if movie_data['imdbVotes'] != 'N/A' else None

            movie_data['DVD'] = str(datetime.strptime(movie_data['DVD'], '%d %b %Y').date()) \
                if movie_data['DVD'] != 'N/A' else None

            movie_data['BoxOffice'] = int(''.join(movie_data['BoxOffice'].split(','))[1:]) \
                if movie_data['BoxOffice'] != 'N/A' else None

            return movie_data
        else:
            return HTTP_404_NOT_FOUND
