from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenVerifyView
app_name = 'accounts-api'
urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    #path("token/login/", CustomeObtainAuthToken.as_view(), name="login")
    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]