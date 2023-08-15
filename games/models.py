from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Game(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(
        to=Genre,
        on_delete=models.PROTECT,
        null=True
    )
    studio = models.ForeignKey(
        to='Studio',
        null=True,
        on_delete=models.PROTECT,
        blank=False
    )

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    workers_count = models.PositiveIntegerField(null=False, verbose_name='Количество работников')
    games_count = models.IntegerField(default=0, verbose_name='Количество игр')

    def __str__(self):
        return self.name

# Create your models here.
