from django.db import models

class MovieWatchList(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()