# Generated by Django 4.2.4 on 2023-08-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('workers_count', models.PositiveIntegerField(verbose_name='Количество работников')),
                ('games_count', models.IntegerField(verbose_name='Количество игр')),
            ],
        ),
    ]