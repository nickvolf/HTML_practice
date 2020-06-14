from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from quiz.models import Word, Quiz
from classroom.models import Classroom


class CustomUser(AbstractUser):
    grade = models.PositiveIntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=30)
    score = models.IntegerField(default=0, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    words = models.ManyToManyField(Word)
    last_test = models.DateTimeField(default=now, blank=True)
    classroom = models.ManyToManyField(Classroom, blank=True)
    has_class = models.BooleanField(default=False)
    streak = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.full_name


class UserQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_passed = models.BooleanField(default=False)
    date_passed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.quiz.quiz_name


class UserTest(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_passed = models.BooleanField(default=False)
    date_passed = models.DateField(null=True, blank=True)
