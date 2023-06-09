import requests
import json
from django.http import JsonResponse
from .models import Movie

# Create your views here.
def trending_movies_week(request):
    # api_key = 'b612e196camshb5467c8057aa232p1c0346jsnd4a71fa248c3' 
    api_key = '1e01e5c9f102f95e9f3cf4d967cf1934'
    url = 'https://api.themoviedb.org/3/trending/movie/week?language=en-US'

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTAxZTVjOWYxMDJmOTVlOWYzY2Y0ZDk2N2NmMTkzNCIsInN1YiI6IjY0ODMzNjA0OTkyNTljMDEzOTJhOTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BsHwAFp2ciEklwqRRkShGybDCZgeNKeWU3l64bawy1Q'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        results = data.get('results', [])

        movies = []
        for entry in results:
            movie = Movie(
                movie_id = entry.get('id'),
                overview = entry.get('overview'),
                poster_path = entry.get('poster_path'),
                title = entry.get('title'),
            )
            movies.append(movie)

        movies_data = [movie.to_dict() for movie in movies]
        movies_json = json.dumps(movies_data, indent=4)

        return JsonResponse({'movies': movies_json})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'API Request Failed: ' + str(e)}, status=500)
