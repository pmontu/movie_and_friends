from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Rating(models.Model):
    STAR_CONVERSION = (
            (1, 'one'),
            (2, 'two'),
            (3, 'three'),
            (4, 'four'),
            (5, 'five'),
        )
    rating = models.PositiveSmallIntegerField(
        choices=STAR_CONVERSION,
        blank=False)
    movie = models.ForeignKey(Movie, blank=False)
    review = models.CharField(max_length=2000)