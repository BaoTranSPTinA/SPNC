from django.db import models
from django.contrib.auth.models import User


class Algorithm(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tutorial(models.Model):
    algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE, related_name="tutorials")
    title = models.CharField(max_length=160)
    media_url = models.URLField(blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title


class Game(models.Model):
    algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE, related_name="games")
    description = models.TextField(blank=True)
    level = models.CharField(max_length=40, default="easy")
    max_score = models.PositiveIntegerField(default=100)

    def __str__(self) -> str:
        return f"Game {self.id} - {self.algo.name}"


class GameAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="attempts")
    score = models.IntegerField(default=0)
    time_spent = models.IntegerField(default=0)
    attempt_date = models.DateTimeField(auto_now_add=True)


class Simulation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    input_data = models.TextField(blank=True)
    output_data = models.TextField(blank=True)
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    completed_part = models.CharField(max_length=120, blank=True)
    last_access = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algo = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)


# Create your models here.
