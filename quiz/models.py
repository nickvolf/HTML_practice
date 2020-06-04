from django.db import models
from django.shortcuts import reverse

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=10)
    quiz_display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz_name

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})


class MCImage(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)


class ChooseWordQuestion(models.Model):
    image = models.ForeignKey(MCImage, on_delete=models.CASCADE)
    sentence_text_pre = models.CharField(max_length=120)
    sentence_text_post = models.CharField(max_length=120)
    correct_answer = models.CharField(max_length=20)
    wrong_asnwer1 = models.CharField(max_length=20)
    wrong_asnwer2 = models.CharField(max_length=20)
    wrong_asnwer3 = models.CharField(max_length=20)
    points = models.PositiveIntegerField()


class ChooseSentenceQuestion(models.Model):
    image = models.ForeignKey(MCImage, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=120)
    wrong_asnwer1 = models.CharField(max_length=120)
    wrong_asnwer2 = models.CharField(max_length=120)
    wrong_asnwer3 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()


class PosNegQuestion(models.Model):
    image = models.ForeignKey(MCImage, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=120)
    wrong_asnwer1 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()


class ResponseQuestion(models.Model):
    image = models.ForeignKey(MCImage, on_delete=models.CASCADE)
    question = models.CharField(max_length=120)
    correct_answer = models.CharField(max_length=120)
    wrong_asnwer1 = models.CharField(max_length=120)
    points = models.PositiveIntegerField()
