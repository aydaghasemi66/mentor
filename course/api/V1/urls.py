from django.urls import path, include
from .views import *


app_name = 'course-api'

urlpatterns = [
    path("courses/",course_api,name='course_api'),
    path("course-detail/<int:pk>/",course_api_detail,name='course_api_detail'),

]