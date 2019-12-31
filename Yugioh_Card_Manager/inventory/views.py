from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Monster, Magic, Trap, Card
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import MonsterSerializer, MagicSerializer, TrapSerializer
from rest_framework.response import Response


class CardsView(LoginRequiredMixin, ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'monster_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CardsView, self).get_context_data(**kwargs)
        context.update({
            'magic_list': Magic.objects.order_by('name'),
            'trap_list': Trap.objects.order_by('name')
        })
        return context

    def get_queryset(self):
        return Monster.objects.all()


class MonsterAPIView(LoginRequiredMixin, CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = MonsterSerializer

    def get_queryset(self):
        return Monster.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# DetailView, CreateView, FormView
class MonsterView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    template_name = 'inventory/detail.html'
    lookup_field = 'pk'
    serializer_class = MonsterSerializer

    def get_queryset(self):
        return Monster.objects.all()


class MagicDetailView(LoginRequiredMixin, DetailView):
    model = Magic
    template_name = 'inventory/detail.html'


class TrapDetailView(LoginRequiredMixin, DetailView):
    model = Trap
    template_name = 'inventory/detail.html'


# class MonsterList(LoginRequiredMixin, APIView):
#     def get(self, request):
#         """
#         List all monster cards.
#         """
#         monsters = Monster.objects.order_by('name')
#         return Response(monsters)

    # def post(self, request):
    #     """
    #     Add a new monster card.
    #     """
    #

# @login_required(login_url='/accounts/login')
# def cards(request, pk):


# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'inventory/help.html', context=helpdict)

# def detail(request, card_id):
#     card = get_object_or_404(Card, pk=card_id)
#     return render(request, 'inventory/detail.html', {'card': card})

# def strategies(requrest, card_id):
#     strategies = "You're looking at the strategic use of the card %s."
#     return HttpResponse(strategies % card_id)