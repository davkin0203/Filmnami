import requests
import json
from django.http import JsonResponse
from .models import Movie, MovieDetails

api_key = '1e01e5c9f102f95e9f3cf4d967cf1934'

def specified_movies(request):
    page = request.GET.get('page') or 1
    type = request.GET.get('type') or 'popular'
    url = f'https://api.themoviedb.org/3/movie/{type}?language=en-US&page={page}'

    return fetch_movies(url)

def specific_movie(request):
    id = request.GET.get('movie_id') or 17473
    url = f'https://api.themoviedb.org/3/movie/{id}?language=en-US'

    return fetch_movie_details(url)

def search_movies(request):
    query = request.GET.get('query','')
    page = request.GET.get('page', '1')

    if query:
        url = f'https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page={page}'

        return fetch_movies(url)
    else:
        return JsonResponse({'error' : 'an error occured'})
    

def fetch_movies(url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTAxZTVjOWYxMDJmOTVlOWYzY2Y0ZDk2N2NmMTkzNCIsInN1YiI6IjY0ODMzNjA0OTkyNTljMDEzOTJhOTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BsHwAFp2ciEklwqRRkShGybDCZgeNKeWU3l64bawy1Q'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        results = data.get('results', [])

        movies = []
        for entry in results:
            movie = Movie (
                movie_id = entry.get('id'),
                poster_path = entry.get('poster_path'),
                title = entry.get('title'),
            )
            movies.append(movie)

        movies_data = [movie.to_dict() for movie in movies]
        movies_json = json.dumps(movies_data)

        return JsonResponse({'movies': movies_json})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'API Request Failed: ' + str(e)}, status=500)

def fetch_movie_details(url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTAxZTVjOWYxMDJmOTVlOWYzY2Y0ZDk2N2NmMTkzNCIsInN1YiI6IjY0ODMzNjA0OTkyNTljMDEzOTJhOTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BsHwAFp2ciEklwqRRkShGybDCZgeNKeWU3l64bawy1Q'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        movie = MovieDetails (
            movie_id = data.get('id'),
            poster_path = data.get('poster_path'),
            title = data.get('title'),
            overview = data.get('overview'),
            release_date = data.get('release_date'),
            runtime = data.get('runtime'),
            vote_average = data.get('vote_average'),
        )

        movies_data = [movie.to_dict()]
        movies_json = json.dumps(movies_data)

        return JsonResponse({'details': movies_json})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'API Request Failed: ' + str(e)}, status=500)