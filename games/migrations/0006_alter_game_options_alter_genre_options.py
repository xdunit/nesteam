# Generated by Django 4.2.4 on 2023-08-21 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_studio_games_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['id']},
        ),
    ]
