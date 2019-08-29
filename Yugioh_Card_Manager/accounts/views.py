from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm


def index(request):
    """
    View for user home page.
    """
    return render(request, 'accounts/index.html')

def user_signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            # Creates hashed password from raw password
            user.set_password(signup_form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account successfully created!')
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
                messages.success(request, 'Successfully logged in!')
                return render(request, 'accounts/home.html')
            else:
                print('Invalid authentication. Please try again.')
        except Exception as e:
            print('User does not exist.')
    return render(request, 'accounts/login.html')

# def user_logout(request):
#     logout(request)