from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class RegistrationView(GenericAPIView):
  serializer = RegisterationSerializer
  def post(self, request, *args, **kwargs):
    serializer = RegisterationSerializer(data=request.data)