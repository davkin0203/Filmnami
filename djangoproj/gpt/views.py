from django.shortcuts import render
import requests
from django.shortcuts import HttpResponse
import json
from movie_display.models import Movie
import json
from django.http import JsonResponse

OPENAI_API_KEY = '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'

def gpt(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }

    user_input = request.GET.get('input')
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'You are a user seeking movie recommendations based on preferences. Return just the movie title.'},
            {'role': 'user', 'content': user_input},
        ],
        'temperature': 0.7,
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()

        recommended_movies = result['choices'][0]['message']['content']
        if recommended_movies:
            movies = [movie.strip() for movie in recommended_movies.split('\n')]

            return fetch_movies(movies)
        else:
            return HttpResponse('no movies reecommended')
    else:
        return HttpResponse('error occured')
    

def fetch_movies(list):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTAxZTVjOWYxMDJmOTVlOWYzY2Y0ZDk2N2NmMTkzNCIsInN1YiI6IjY0ODMzNjA0OTkyNTljMDEzOTJhOTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BsHwAFp2ciEklwqRRkShGybDCZgeNKeWU3l64bawy1Q'
        }

        results_list = []
        for movie in list:
            url = f'https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1'
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            results = data.get('results', [])
            results_list.extend(results)

        movies = []
        for entry in results_list:
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