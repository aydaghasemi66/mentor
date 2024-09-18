from django.urls import path, include
from .views import *


app_name = 'course-api'

urlpatterns = [
    path("courses/",CourseApiView.as_view(),name='course_api'),
    path("course-detail/<int:pk>/",CourseDetailView.as_view(),name='course_api_detail'),

]