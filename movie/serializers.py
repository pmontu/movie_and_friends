from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=200)
	class Meta:
		fields = ["name",]