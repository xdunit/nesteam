from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, verbose_name='Имя пользователя')
    email = models.EmailField(null=True, blank=True, verbose_name='@mail')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Player(models.Model):
    nick = models.CharField(max_length=200)

# Create your models here.
