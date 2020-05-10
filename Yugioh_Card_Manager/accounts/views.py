from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm


def index(request):
    """
    View for website home page.
    """
    return render(request, 'accounts/home.html')

def user_signup(request):
    """
    View for sign up page.
    """
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            # Creates hashed password from raw password
            user.set_password(signup_form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/signup_success.html')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})

def user_login(request):
    """
    View for login page.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                # messages.success(request, 'Successfully logged in!')
                # TODO: use redirect to different url instead of render
                return render(request, 'accounts/user_home.html')
            else:
                # TODO: fix message display (clear it after each run)
                messages.error(request, 'Invalid authentication. Please try again.')
        except Exception as e:
            messages.error(request, 'User does not exist. Please try again.')
    return render(request, 'accounts/login.html')

def user_home(request):
    """
    View for user home page.
    """
    # TODO: Check if user homepage is displayed only when authenticated.
    # (Right now renders the page when we click 'Back' from 'View all cards'.)
    return render(request, 'accounts/user_home.html')

def user_logout(request):
    """
    View for logout page.
    """
    logout(request)
    return render(request, 'accounts/logout_success.html')