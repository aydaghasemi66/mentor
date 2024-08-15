from django.urls import path, include
from .views import *


app_name = "accounts"


urlpatterns = [
    path("login/", Login, name="login"),
    path("signup/", Signup, name="signup"),

]