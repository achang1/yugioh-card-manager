from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login')
]