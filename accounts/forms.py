from django import forms
from django.contrib.auth.forms import UserCreationForm   
from .models import CustomeUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ('email', 'password1','username', 'password2')


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label= ("Password"),
        strip= False,
        widget=forms.PasswordInput(attrs={'autocomplete': "current-password"}),
    )

class Edit_Profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ["user", "first_name", "last_name", "image", "number", "address"]
