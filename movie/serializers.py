from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        movie = Movie(**validated_data)
        movie.save()
        return movie
