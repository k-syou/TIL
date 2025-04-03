from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def index(request: HttpRequest):
    users = get_user_model().objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)

def login(request: HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required(login_url='accounts:login')
def logout(request: HttpRequest):
    auth_logout(request)
    return redirect('accounts:index')

def signup(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()   
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='accounts:login')
def delete(request: HttpRequest):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

@login_required(login_url='accounts:login')
def update(request: HttpRequest):   
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required(login_url='accounts:login')
def change_password(request: HttpRequest, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 비밀번호 변경 후 세션 연장
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
