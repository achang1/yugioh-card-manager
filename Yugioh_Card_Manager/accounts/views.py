from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from accounts.forms import SignUpForm


def index(request):
    """
    View for user home page.
    """
    return render(request, 'accounts/index.html')

def login(request):
    """
    View for login page.
    """
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            # Creates hashed password from raw password
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Account successfully created!')
            # TODO: redirect to page. Using render, path is still signup using login template
            return render(request, 'accounts/login.html')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})