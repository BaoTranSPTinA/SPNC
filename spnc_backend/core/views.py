from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Algorithm, Tutorial, Game, Progress, GameAttempt
from django.shortcuts import render
from .serializers import (
    AlgorithmSerializer,
    TutorialSerializer,
    GameSerializer,
    ProgressSerializer,
    GameAttemptSerializer,
)


class AlgorithmListCreateView(generics.ListCreateAPIView):
    queryset = Algorithm.objects.all().order_by("id")
    serializer_class = AlgorithmSerializer


class TutorialListCreateView(generics.ListCreateAPIView):
    serializer_class = TutorialSerializer

    def get_queryset(self):
        qs = Tutorial.objects.all().order_by("id")
        algo_id = self.request.query_params.get("algo")
        return qs.filter(algo_id=algo_id) if algo_id else qs


class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by("id")
    serializer_class = GameSerializer


@api_view(["GET"])
def health(_request):
    return Response({"status": "ok"})


class ProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user).order_by("-last_access")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GameAttemptListCreateView(generics.ListCreateAPIView):
    serializer_class = GameAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GameAttempt.objects.filter(user=self.request.user).order_by("-attempt_date")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def algorithms(request):
    return render(request, 'pages/algorithms.html')

def tutorials(request):
    return render(request, 'pages/tutorials.html')

def games(request):
    return render(request, 'pages/games.html')

def login_view(request):
    return render(request, 'pages/login.html')