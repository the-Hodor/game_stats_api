from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, related_name="reviews", on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Review for {self.game.title} - {self.rating}/10"
