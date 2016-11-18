from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User


class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    id = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField()

    def create(self, validated_data):
        movie = Movie(**validated_data)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    def get_average_rating(self, obj):
        return 0 if obj.sum_ratings is None else obj.sum_ratings / float(obj.count_ratings)


class RatingPostSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    id = serializers.ReadOnlyField()
    movie_name = serializers.SerializerMethodField()

    def create(self, validated_data):
        rating = Rating(**validated_data)
        rating.save()
        return rating
    
    def get_movie_name(self, obj):
        return obj.movie.name


class RatingSerializer(serializers.Serializer):
    rating = serializers.ChoiceField(Rating.STAR_CONVERSION)
    movie = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        instance.rating = validated_data.get("rating", instance.rating)
        instance.save()
        return instance

