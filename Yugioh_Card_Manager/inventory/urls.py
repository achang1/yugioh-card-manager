from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('cards', views.CardsView.as_view(), name='cards'),
    path('monster', views.MonsterAPIView.as_view(), name='monster_create'),
    path('monster/<int:pk>', views.MonsterCrudView.as_view(), name='monster_crud'),
    path('magic/<int:pk>', views.MagicDetailView.as_view(), name='magic_detail'),
    path('trap/<int:pk>', views.TrapDetailView.as_view(), name='trap_detail'),
]