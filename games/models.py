from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Create your models here.
