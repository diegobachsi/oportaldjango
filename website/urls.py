from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.videos, name='videos'),
    path('contato/', views.contact, name='contato'),
    path('config/', views.config, name='config'),
    path('session_gamer/', views.sessiongamer, name='session_gamer'),
    path('alterar_tema/', views.alterar_tema, name='alterar_tema'),
]