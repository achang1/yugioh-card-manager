from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('home', views.index, name='home'),
    path('signup', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('user_home', views.user_home, name='user_home'),
]