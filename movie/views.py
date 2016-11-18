from rest_framework import viewsets, mixins, permissions
from .models import Movie, Rating
from .serializers import (
    RatingSerializer, MovieSerializer, RatingPostSerializer)
from utils.mixins import MultiSerializerViewSetMixin
from django.db.models.aggregates import Sum, Count
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

class MovieViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Movie.objects.annotate(sum_ratings=Sum("rating"),count_ratings=Count("rating"))
    serializer_class = MovieSerializer


class RatingViewSet(
    MultiSerializerViewSetMixin,
    viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = RatingPostSerializer
    serializer_action_classes = {
               'update': RatingSerializer
            }

    def get_queryset(self):
        return Rating.objects.filter(
            movie__id=self.kwargs["movie"])
