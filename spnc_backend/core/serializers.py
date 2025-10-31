from rest_framework import serializers
from .models import Algorithm, Tutorial, Game, Progress, GameAttempt


class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ["id", "name", "description", "type", "created_at"]


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ["id", "algo_id", "title", "media_url", "content"]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "algo_id", "description", "level", "max_score"]


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ["id", "algo_id", "completed_part", "last_access"]


class GameAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameAttempt
        fields = ["id", "game_id", "score", "time_spent", "attempt_date"]


