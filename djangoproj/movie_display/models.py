from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.CharField(max_length=100, default='')
    # contained in primaryImage
    image_id = models.CharField(max_length=100, default='')
    # contained in titleText
    title_text = models.CharField(max_length=100, default='')

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'image_id': self.image_id,
            'title_text': self.title_text,
        }

    def __str__(this):
        return this.title_text