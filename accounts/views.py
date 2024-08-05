from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from root.views import home
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.


def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def loginview(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def logoutview(request):
    logout(request)
    messages.success(request, 'logout successfully', 'success')
    return redirect('/')
