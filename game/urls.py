from django.urls import path
from . import views

urlpatterns = [
    path('', views.snake_game, name='snake_game'),
    path('save_score/', views.save_score, name='save_score'),
]
