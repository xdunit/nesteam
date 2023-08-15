# Generated by Django 4.2.4 on 2023-08-14 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('franchise', '0003_alter_gamecollection_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecollection',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_collection', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='gamecollection',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_collection', to=settings.AUTH_USER_MODEL),
        ),
    ]
