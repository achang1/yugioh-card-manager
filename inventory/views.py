from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Monster, Magic, Trap
from .forms import SignUpForm


def index(request):
    """
    View for user home page.
    """
    return render(request, 'inventory/index.html')

def login(request):
    """
    View for login page.
    """
    return render(request, 'inventory/login.html')

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
            return render(request, 'inventory/login.html')
    else:
        signup_form = SignUpForm()
    return render(request, 'inventory/signup.html', {'signup_form': signup_form})

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'inventory/help.html', context=helpdict)

# def detail(request, card_id):
#     card = get_object_or_404(Card, pk=card_id)
#     return render(request, 'inventory/detail.html', {'card': card})

# def strategies(requrest, card_id):
#     strategies = "You're looking at the strategic use of the card %s."
#     return HttpResponse(strategies % card_id)