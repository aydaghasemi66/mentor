from ...models import CustomeUser
from rest_framework import serializers

class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ["email", "username", "password", "password1"]