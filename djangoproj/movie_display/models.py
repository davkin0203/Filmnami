from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(default=0)
    # contained in primaryImage
    overview = models.CharField(max_length=100, default='')
    # contained in primaryImage
    poster_path = models.CharField(max_length=100, default='https://preview.redd.it/ivgqylh7zho41.png?width=1080&crop=smart&auto=webp&v=enabled&s=6a3d851aa2ee71e21ce5a888e01efc42a72b33b3')
    # contained in titleText
    title = models.CharField(max_length=100, default='')

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'overview': self.overview,
            'poster_path': self.poster_path,
            'title': self.title,
        }

    def __str__(this):
        return this.title