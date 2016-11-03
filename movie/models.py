from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=200)

class Rating(models.Model):
	STAR_CONVERSION = (
            (1, 'one'),
            (2, 'two'),
            (3, 'three'),
            (4, 'four'),
            (5, 'five'),
        )
	value = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)
	movie = models.ForeignKey(Movie)
	text = models.CharField(max_length=2000)