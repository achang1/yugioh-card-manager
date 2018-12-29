from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Card

def index(request):
    return HttpResponse("Search for your cards hereeeeee.")

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'search/help.html', context=helpdict)

def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'search/detail.html', {'card': card})

def strategies(requrest, card_id):
    strategies = "You're looking at the strategic use of the card %s."
    return HttpResponse(strategies % card_id)