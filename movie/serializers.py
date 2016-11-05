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


class RatingSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    id = serializers.ReadOnlyField()
    movie = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name")


class RatingSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    def create(self, validated_data):
        rating = Rating(**validated_data)
        rating.save()
        return rating

