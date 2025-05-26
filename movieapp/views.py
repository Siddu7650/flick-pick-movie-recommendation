from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Movie
from .serializers import MovieSerializer

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]