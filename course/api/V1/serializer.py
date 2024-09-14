from rest_framework import serializers

class CourseApiSerializer(serializers.Serializer):
    id= serializers.ImageField()
    title= serializers.CharField(max_length=200)
    price= serializers.ImageField()
    