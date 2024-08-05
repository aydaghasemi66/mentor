from django.urls import path
from .views import signupview, loginview, logoutview

app_name = 'accounts'


urlpatterns = [
    path("signup/",signupview,name="signup"),
    path("login/", loginview, name="login"),
    path("logout/", logoutview, name="logout"),
]