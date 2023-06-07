import requests
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
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
                image_id = entry.get("primaryImage", {}).get('id') if entry.get("primaryImage") else None,
                title_text = entry.get("titleText", {}).get('text'),
            )
            movies.append(movie)

        movies_data = [movie.to_dict() for movie in movies]
        movies_json = json.dumps(movies_data, indent=4)

        return HttpResponse({'movies': movies_json})
    else:
        return HttpResponse({'error' : 'API Request Failed'}, status = response.status_code)
