# Generated by Django 4.2.4 on 2023-08-20 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_player'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]