from django.db import models

# Create your models here.

class HighScore(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player_name} - {self.score}"
