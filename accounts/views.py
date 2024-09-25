from django.shortcuts import render, redirect
from .forms import AuthenticationForm, CustomUserCreationForm , Edit_Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
# Create your views here.
def Login(request):
    if request.user.is_authenticated :
        return redirect('/')
    elif request.method == 'Get':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    elif request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'registration/login.html', {'form': form})
        


def Signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request,'registration/signup.html', context={'form': form})
    else:
            form = CustomUserCreationForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                email = request.POST.get('email')
                password = request.POST.get('password1')
                user = authenticate(email=email, password=password)
                login(request,user)
                return redirect('/')

            else:
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                return redirect(request.path_info)
            
def edit_profile(request, pk):
      if request.method == 'GET':
           form = Edit_Profile()
           return render(request,'registration/edit_profile.html', context={'form': form})
      elif request.method == 'POST':
           profile = Profile.objects.get(user=pk)
           form = Edit_Profile(request.POST, request.FILES, instance=profile)
           if form.is_valid():
                form.save()
                return redirect('root:home')
           

