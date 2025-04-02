from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request: HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request: HttpRequest):
    auth_logout(request)
    return redirect('articles:index')

def signup(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()   
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

