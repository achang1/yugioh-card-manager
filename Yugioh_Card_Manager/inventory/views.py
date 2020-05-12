from django.db.models import Q
from .models import Monster, Magic, Trap
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import MonsterSerializer, MagicSerializer, TrapSerializer
from .permissions import IsOwnerOrReadOnly


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
        return Monster.objects.filter(user=self.request.user)


class MonsterAPIView(CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = MonsterSerializer

    def get_queryset(self):
        queryset = Monster.objects.filter(user=self.request.user)
        # query = self.request.GET.get("q")
        # if query is not None:
        #     queryset = queryset.filter(Q(name__icontains=query)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MonsterRudView(RetrieveUpdateDestroyAPIView):
    # template_name = 'inventory/detail.html'
    lookup_field = 'pk'
    serializer_class = MonsterSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Monster.objects.filter(user=self.request.user)


class MagicAPIView(CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = MagicSerializer

    def get_queryset(self):
        queryset = Magic.objects.filter(user=self.request.user)
        # query = self.request.GET.get("q")
        # if query is not None:
        #     queryset = queryset.filter(Q(name__icontains=query)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MagicRudView(RetrieveUpdateDestroyAPIView):
    # template_name = 'inventory/detail.html'
    lookup_field = 'pk'
    serializer_class = MagicSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Magic.objects.filter(user=self.request.user)


class TrapAPIView(CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = TrapSerializer

    def get_queryset(self):
        queryset = Trap.objects.filter(user=self.request.user)
        # query = self.request.GET.get("q")
        # if query is not None:
        #     queryset = queryset.filter(Q(name__icontains=query)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TrapRudView(RetrieveUpdateDestroyAPIView):
    # template_name = 'inventory/detail.html'
    lookup_field = 'pk'
    serializer_class = TrapSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Trap.objects.filter(user=self.request.user)