from django.urls import path
from django.views.generic import TemplateView

"""
URL configuration for movie_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_display.views import trending_movies_week
from gpt.views import gpt
from search_movies.views import search_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', trending_movies_week, name='trending_movies_week'),
    path('gpt/', gpt, name='gpt'),
    path('search/', search_movies, name='search_movies')
]