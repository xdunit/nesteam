from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    workers_count = models.PositiveIntegerField(null=False, verbose_name='Количество работников')
    games_count = models.IntegerField(null=False, blank=False, verbose_name='Количество игр')

    def __str__(self):
        return self.name

# Create your models here.
