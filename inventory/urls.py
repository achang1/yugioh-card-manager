from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('signup', views.signup, name='signup'),
#     path('<int:card_id>', views.detail, name='detail'),
#     path('<int:card_id>/strategies/', views.strategies, name='strategies')
]