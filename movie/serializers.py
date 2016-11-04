from rest_framework import serializers
from .models import Movie, Rating
from datetime import datetime
import pytz

class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        movie = Movie(**validated_data)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
    
    class Meta:
        model = Movie
        fields = ["id", "name"]


class RatingSeriallizer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    id = serializers.ReadOnlyField()
    movie = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name")

    def create(self, validated_data):
        import ipdb; ipdb.set_trace()
        validated_data["movie"] = Movie.objects.get(id=validated_data["movie"])
        rating = Rating(**validated_data)
        rating.created = datetime.now(pytz.UTC)
        rating.modified = datetime.now(pytz.UTC)
        rating.save()
        return rating


class RatingPostSeriallizer(serializers.Serializer):
    # rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    # id = serializers.ReadOnlyField()
    # movie = MovieSerializer()

    def create(self, validated_data):
        import ipdb; ipdb.set_trace()
        validated_data["movie"] = Movie.objects.get(id=validated_data["movie"])
        rating = Rating(**validated_data)
        rating.created = datetime.now(pytz.UTC)
        rating.modified = datetime.now(pytz.UTC)
        rating.save()
        return rating

    class Meta:
        model = Rating
        fields = ["movie", "rating", "id"]

