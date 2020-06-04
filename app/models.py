from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Classroom(models.Model):
    classroom_name = models.CharField(max_length=30)

    def __str__(self):
        return self.classroom_name

class Word(models.Model):
    english = models.CharField(max_length = 20)
    korean = models.CharField(max_length = 8)

    def __str__(self):
        return self.english