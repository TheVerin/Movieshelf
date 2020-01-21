import json
import requests
from datetime import datetime

from rest_framework.status import HTTP_404_NOT_FOUND

from django.conf import settings


def get_data_from_omdb(title):
    payload = {'t': title, 'apikey': settings.OMBDAPI_KEY}
    movie_data = json.loads(requests.get('http://www.omdbapi.com/', params=payload).text)
    if 'Error' not in movie_data.keys():
        movie_data['Year'] = int(movie_data['Year'])
        movie_data['Runtime'] = int(movie_data['Runtime'].split()[0])
        movie_data['Released'] = str(datetime.strptime(movie_data['Released'], '%d %b %Y').date())
        movie_data['Genre'] = movie_data['Genre'].split(', ')
        movie_data['Director'] = movie_data['Director'].split(', ')
        movie_data['Writer'] = movie_data['Writer'].split(', ')
        movie_data['Actors'] = movie_data['Actors'].split(', ')
        movie_data['Ratings'] = [[rating['Source'], rating['Value']]
                                 for rating in movie_data['Ratings']]
        movie_data['Metascore'] = int(movie_data['Metascore'])
        movie_data['imdbRating'] = float(movie_data['imdbRating'])
        movie_data['imdbVotes'] = int(''.join(movie_data['imdbVotes'].split(',')))
        movie_data['DVD'] = str(datetime.strptime(movie_data['DVD'], '%d %b %Y').date())
        movie_data['BoxOffice'] = int(''.join(movie_data['BoxOffice'].split(','))[1:])
        return movie_data
    else:
        return HTTP_404_NOT_FOUND
