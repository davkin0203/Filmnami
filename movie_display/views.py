import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

# Create your views here.
def get_movie_data(request):
    api_key = 'b612e196camshb5467c8057aa232p1c0346jsnd4a71fa248c3' 
    url = 'https://moviesdatabase.p.rapidapi.com/titles'

    headers = {
        "X-RapidAPI-Key": "b612e196camshb5467c8057aa232p1c0346jsnd4a71fa248c3",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])

        movies = []
        for entry in results:
            movie = Movie(
                movie_id = entry.get('id'),
                image_id = entry.get("primaryImage", {}).get('id'),
                title_text = entry.get("titleText", {}).get('text'),
            )
            movies.append(movie)
        
        return JsonResponse({'movies' : movies})
    else:
        return JsonResponse({'error' : 'API Request Failed'}, status = response.status_code)
