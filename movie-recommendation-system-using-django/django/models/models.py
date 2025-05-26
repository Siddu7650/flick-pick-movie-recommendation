from django.db import models
from django.contrib.auth.models import User

RATING_CHOICES = [
    (1, 'Very Bad'),
    (2, 'Bad/Overrated'),
    (3, 'Average'),
    (4, 'Pretty Good'),
    (5, 'Fantastic'),
]

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    awards = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} - {self.rating}"
