from rest_framework import serializers
from ...models import *




class CourseSerializer(serializers.ModelSerializer):

    #teacher = serializers.ReadOnlyField()
    content = serializers.ReadOnlyField()
    # detail_link = serializers.SerializerMethodField(method_name='detail')
    price= serializers.SerializerMethodField(method_name="detail")
    detail_link= serializers.SerializerMethodField(method_name="detail")
    class Meta:
        model = Course
        fields = ["title", "price", "content", "category", "teacher", "image", 'status','detail_link']

    def get_price(self, obj):
        return obj.price * 50000
    # def detail(self,obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.id)
    # def get_description(self,obj):
    #     return obj.description[:100] + '...'
    # def detail(self,obj):
    #     return obj.description[:100] + '...'
    def detail(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['teacher'] = TrainerSerializer(instance.teacher).data
        rep['category'] = CategorySerializer(instance.category, many=True).data
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is not None:
            rep.pop('content')
        return rep
    
class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","title", "content",]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title"]


        

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["id", "name"]



class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'