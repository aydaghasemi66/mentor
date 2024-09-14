from django.urls import path, include
from .views import *


app_name = 'course-api'

urlpatterns = [
    path("",course_api,name='course_api'),

]