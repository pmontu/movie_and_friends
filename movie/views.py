from rest_framework import viewsets, mixins
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(
	mixins.DestroyModelMixin,
	mixins.CreateModelMixin,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer