import requests
from django.http import JsonResponse

def search_movies(request):
    query = request.GET.get('query','')
    page = request.GET.get('page', '1')

    if query:
        url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page={page}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTAxZTVjOWYxMDJmOTVlOWYzY2Y0ZDk2N2NmMTkzNCIsInN1YiI6IjY0ODMzNjA0OTkyNTljMDEzOTJhOTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BsHwAFp2ciEklwqRRkShGybDCZgeNKeWU3l64bawy1Q"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()

            return JsonResponse(result)
    else:
        return JsonResponse({'error' : 'an error occured'})