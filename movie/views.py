from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer