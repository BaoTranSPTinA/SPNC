from django.contrib import admin
from .models import Algorithm, Tutorial, Game, GameAttempt, Simulation, Progress, Feedback

admin.site.register(Algorithm)
admin.site.register(Tutorial)
admin.site.register(Game)
admin.site.register(GameAttempt)
admin.site.register(Simulation)
admin.site.register(Progress)
admin.site.register(Feedback)

# Register your models here.
