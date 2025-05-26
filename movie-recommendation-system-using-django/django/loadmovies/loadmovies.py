import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommendation_project.settings')
django.setup()

from movie_recommender.models import Movie

movies = [
    {"title": "Jurassic Park", "director": "Steven Spielberg", "awards": "Academy Award for Best Sound"},
    {"title": "Saving Private Ryan", "director": "Steven Spielberg", "awards": "5 Academy Awards"},
    {"title": "Titanic", "director": "James Cameron", "awards": "11 Academy Awards"},
    {"title": "Avatar", "director": "James Cameron", "awards": "3 Academy Awards"},
    {"title": "Inception", "director": "Christopher Nolan", "awards": "4 Academy Awards"},
    {"title": "Interstellar", "director": "Christopher Nolan", "awards": "Academy Award for Best Visual Effects"},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "awards": "Palme d'Or, Academy Award for Best Original Screenplay"},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "awards": "3 Academy Awards"},
    {"title": "Apocalypse Now", "director": "Francis Ford Coppola", "awards": "2 Academy Awards"},
    {"title": "2001: A Space Odyssey", "director": "Stanley Kubrick", "awards": "Academy Award for Best Visual Effects"},
    {"title": "The Shining", "director": "Stanley Kubrick", "awards": "Saturn Award for Best Horror Film"},
    {"title": "Seven Samurai", "director": "Akira Kurosawa", "awards": "Silver Lion for Best Director"},
    {"title": "Rashomon", "director": "Akira Kurosawa", "awards": "Academy Honorary Award"},
    {"title": "Psycho", "director": "Alfred Hitchcock", "awards": "Academy Award nominations for Best Director, etc."},
    {"title": "Vertigo", "director": "Alfred Hitchcock", "awards": "Sight & Sound Best Film 2012"},
    {"title": "Goodfellas", "director": "Martin Scorsese", "awards": "Academy Award for Best Supporting Actor"},
    {"title": "Taxi Driver", "director": "Martin Scorsese", "awards": "Palme d'Or"},
]

for movie in movies:
    Movie.objects.get_or_create(
        title=movie["title"],
        director=movie["director"],
        awards=movie["awards"]
    )

print("✅ Movie data loaded successfully.")
