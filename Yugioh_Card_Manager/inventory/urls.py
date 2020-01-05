from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('cards', views.CardsView.as_view(), name='cards'),
    path('monster', views.MonsterAPIView.as_view(), name='monster_create'),
    path('monster/<int:pk>', views.MonsterRudView.as_view(), name='monster_rud'),
    path('magic', views.MagicAPIView.as_view(), name='magic_create'),
    path('magic/<int:pk>', views.MagicRudView.as_view(), name='magic_rud'),
    path('trap', views.TrapAPIView.as_view(), name='trap_create'),
    path('trap/<int:pk>', views.TrapRudView.as_view(), name='trap_rud'),
]