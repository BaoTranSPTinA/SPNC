from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health),
    path('algorithms/', views.AlgorithmListCreateView.as_view()),
    path('tutorials/', views.TutorialListCreateView.as_view()),
    path('games/', views.GameListCreateView.as_view()),
    path('progress/', views.ProgressListCreateView.as_view()),
    path('attempts/', views.GameAttemptListCreateView.as_view()),
]


