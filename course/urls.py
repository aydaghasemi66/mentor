from django.urls import path, include
from .views import *


app_name = 'course'

urlpatterns = [
    path("",courses,name='courses'),
    path("category/<str:cat>", courses, name='courses_by_category'),
    path("trainers/<str:trainer>", courses, name='courses_by_trainer'),
    path("search/", courses, name='courses_by_search'),
    path("course_detail/<int:id>", course_detail, name='course_detail'),
    path("comment/reply/<int:id>",reply,name="reply"),
]