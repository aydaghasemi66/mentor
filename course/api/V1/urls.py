from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'course-api'

router = DefaultRouter()
router.register('courses', CourseView, basename='courses')
router.register('categories', CategoryView, basename='categories')
router.register('skills', CategoryView, basename='skills')
router.register('trainer', TrainerView, basename='trainer')
urlpatterns = router.urls



# urlpatterns = [
#     path("courses/",CourseView.as_view({'get': 'list', 'post':'create'}),name='courses'),
#     path("courses/<int:pk>/",CourseView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='course-detail'),

# ]