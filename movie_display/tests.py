from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse
from movie_display.models import Movie

class MovieDataTest(TestCase):
    @patch('movie_display.views.requests.get')
    def test_get_movie_data(self, mock_get):
        # Mock the response from the API
        mock_response = {
            'results': [
                {
                    'id': 'tt0000081',
                    'primaryImage': {'id': 'rm211543552'},
                    'titleText': {'text': 'Les haleurs de bateaux (1896)'}
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Make the API call
        response = self.client.get(reverse('movies/'))

        # Assert the response and processed data
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            'movies': [
                {
                    'movie_id': 'tt0000081',
                    'image_id': 'rm211543552',
                    'title_text': 'Les haleurs de bateaux (1896)'
                }
            ]
        })