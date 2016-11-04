from rest_framework import serializers
from .models import Movie

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
