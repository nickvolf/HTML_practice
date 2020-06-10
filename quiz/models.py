from django.db import models
from django.shortcuts import reverse
from books.models import Unit


class Quiz(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=10)
    quiz_display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz_name

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})


class MCImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.description


class ChooseWordQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ForeignKey(MCImage, null=True, blank=True, on_delete=models.SET_NULL)
    sentence_text_pre = models.CharField(max_length=120)
    sentence_text_post = models.CharField(max_length=120)
    correct_answer = models.CharField(max_length=20)
    wrong_answer1 = models.CharField(max_length=20)
    wrong_answer2 = models.CharField(max_length=20)
    wrong_answer3 = models.CharField(max_length=20)
    points = models.PositiveIntegerField()


class ChooseSentenceQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ForeignKey(MCImage, null=True, blank=True, on_delete=models.SET_NULL)
    correct_answer = models.CharField(max_length=120)
    wrong_answer1 = models.CharField(max_length=120)
    wrong_answer2 = models.CharField(max_length=120)
    wrong_answer3 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()


class PosNegQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ForeignKey(MCImage, null=True, blank=True, on_delete=models.SET_NULL)
    correct_answer = models.CharField(max_length=120)
    wrong_answer1 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()


class ResponseQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ForeignKey(MCImage, null=True, blank=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=120)
    correct_answer = models.CharField(max_length=120)
    wrong_answer1 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()


class Word(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    english = models.CharField(max_length=20)
    korean = models.CharField(max_length=8)

    def __str__(self):
        return self.english
