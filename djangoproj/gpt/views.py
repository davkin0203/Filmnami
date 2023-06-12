from django.shortcuts import render
import requests

import openai

import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

def gpt(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': 'Say this is a test!'}],
        'temperature': 0.7,
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        # Process the result as needed
        return render(request, 'your_template.html', {'result': result})
    else:
        # Handle error cases
        return render(request, 'error_template.html')