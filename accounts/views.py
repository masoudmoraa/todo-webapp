from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in. Redirected to the home page.", extra_tags="warning")
        return redirect('homepage')
    
    if request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'User registered successfully', extra_tags='success')
            return redirect('homepage')
    else :
        form = UserRegistrationForm()
    return render(request, 'register.html', {"form":form})


def user_login(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in. Redirected to the home page.", extra_tags="warning")
        return redirect('homepage')
    
    if request.method == "POST" :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request, 'user logged in successfully', extra_tags='success')
                return redirect('homepage')
            else:
                messages.error(request, 'Information does not match!', extra_tags='danger')
    else :
        form = UserLoginForm()
    return render(request, 'login.html', {"form":form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'User logged out successfully', extra_tags='success')
    return redirect('user_login')