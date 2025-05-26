from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Flick Pick Paradise Django Backend!")

urlpatterns = [
    path('', home),  # Homepage route
    path('admin/', admin.site.urls),
    path('api/', include('movieapp.urls')),  # or your app's urls
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),  # API endpoints
]