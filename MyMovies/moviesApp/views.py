from django.views.generic import ListView
from moviesApp.models import myMovie

class MovieList(ListView):
    model = myMovie