from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField(default=0)
    poster_path = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'poster_path': self.poster_path,
            'title': self.title,
        }

    def __str__(this):
        return this.title
    
class MovieDetails(models.Model):
    movie_id = models.IntegerField(default=0)
    poster_path = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    overview = models.CharField(max_length=100, default='')
    release_date = models.CharField(max_length=100, default='')
    runtime = models.IntegerField(default=0)
    vote_average = models.IntegerField(default=0)

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'poster_path': self.poster_path,
            'title': self.title,
            'overview': self.overview,
            'release_date': self.release_date,
            'runtime': self.runtime,
            'vote_average': self.vote_average,
        }

    def __str__(this):
        return this.title