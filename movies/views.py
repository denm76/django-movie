from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView, DetailView


# Create your views here.


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"
