from django.urls import path, include
from .views import *


app_name = "accounts"


urlpatterns = [
    path("login/", Login, name="login"),
    path("signup/", Signup, name="signup"),
    path("edit-profile/<int:pk>", edit_profile, name="profile"),
    path('api/V1/accounts',include("accounts.api.V1.urls"))

]