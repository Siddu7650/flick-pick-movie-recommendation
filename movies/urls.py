from django.urls import path
from .views import MovieListCreate, UserCreate, Login

urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]