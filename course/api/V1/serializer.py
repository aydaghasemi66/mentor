from rest_framework import serializers
from ...models import *




class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "title", "content",]


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","title", "content",]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title",]
