from rest_framework import viewsets, mixins
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSeriallizer, RatingPostSeriallizer

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
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    serializer_class = RatingSeriallizer
    serializer_action_classes = {
               'post': RatingPostSeriallizer,
            }

    def create(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        data = request.data.copy()
        # data["movie"] = kwargs["movie_id"]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def get_queryset(self):
        return Rating.objects.filter(
            movie__id=self.kwargs["movie"])


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:
        class MyViewSet(ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }
            @action
            def my_action:
                ...
        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except KeyError:
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()

