# Generated by Django 3.0.3 on 2020-06-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200613_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='streak',
            field=models.PositiveIntegerField(default=0),
        ),
    ]