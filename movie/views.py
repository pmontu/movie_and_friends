from rest_framework import viewsets, mixins
from .models import Movie, Rating
from .serializers import (
    MovieSerializer, RatingSerializer, RatingPostSerializer)
from utils.mixins import MultiSerializerViewSetMixin


class MovieViewSet(
    mixins.UpdateModelMixin,
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

class RatingViewSet(
    MultiSerializerViewSetMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    serializer_class = RatingSerializer
    serializer_action_classes = {
                'list': RatingSerializer,
               'create': RatingPostSerializer,
            }

    def get_queryset(self):
        return Rating.objects.filter(
            movie__id=self.kwargs["movie"])
