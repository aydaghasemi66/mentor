from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Course
from .serializer import CourseApiSerializer
@api_view()
def course_api(request):
    courses = Course.objects.all()
    serializer = CourseApiSerializer(courses, many=True)
    return Response(serializer.data)
