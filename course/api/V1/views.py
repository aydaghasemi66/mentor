from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Course
from .serializer import CourseSerializer, CourseDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

# @api_view()
# def course_api(request):
#     courses = Course.objects.all()
#     course_serializer = CourseSerializer(courses, many=True)
#     return Response(course_serializer.data)


# @api_view(["GET","POST","PUT","DELETE"])
# def course_api_detail(request, pk):
#     course = get_object_or_404(Course, id=pk)
#     if request.method == "GET":
        
#         course_serializer = CourseDetailSerializer(course)
#         return Response(course_serializer.data)
#     elif request.method == "POST":
#         course_serializer = CourseDetailSerializer(data=request.data)
#         if course_serializer.is_valid():
#             course_serializer.save()
#             return Response(course_serializer.data)
#         else:
#             return Response(course_serializer.errors)
#     elif request.method == "PUT":
#         course_serializer = CourseDetailSerializer(data=request.data)
#         if course_serializer.is_valid(raise_exception=True):
#             course_serializer.save()
#             return Response(course_serializer.data)
#     elif request.method == "DELETE":
#         course_serializer = CourseDetailSerializer(data=request.data)
#         if course_serializer.is_valid(raise_exception=True):
#             course.delete()
#             return Response("course deleted successfully", status=status.HTTP_204_NO_CONTENT)


class CourseApiView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(status=True)
        course_serializer = CourseSerializer(courses, many=True)
        return Response(course_serializer.data)

    def post(self, request, *args, **kwargs):
        course_serializer = CourseSerializer(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, id=pk)
        course_serializer = CourseDetailSerializer(course)
        return Response(course_serializer.data) 
    def put(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, id=pk)
        course_serializer = CourseDetailSerializer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        else:
            return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, id=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)