from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('cards', views.CardsView.as_view(), name='cards'),
    path('cards/<int:card_id>', views.CardDetailView.as_view(), name='card_details'),
#     path('<int:card_id>', views.detail, name='detail'),
#     path('<int:card_id>/strategies/', views.strategies, name='strategies')
]