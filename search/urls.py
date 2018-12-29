from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('<int:card_id>', views.detail, name='detail'),
    path('<int:card_id>/strategies/', views.strategies, name='strategies')
]