from rest_framework import serializers
from .models import Movie, Rating

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


class RatingSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    id = serializers.ReadOnlyField()
    movie = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name")


class RatingPostSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    movie = MovieSerializer()

    def create(self, validated_data):
        movie_data = validated_data.pop('movie')
        movie = Movie.objects.get(name=movie_data["name"])
        validated_data["movie"] = movie
        rating = Rating(**validated_data)
        rating.save()
        return rating

