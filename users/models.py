from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import Word
from quiz.models import Quiz

class CustomUser(AbstractUser):
    grade = models.PositiveIntegerField(null=True, blank=True)
    full_name = models.CharField(max_length = 30)
    score = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    words = models.ManyToManyField(Word)
    quizes_passed = models.ManyToManyField(Quiz)
