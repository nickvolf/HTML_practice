from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from quiz.models import Word, Quiz
from classroom.models import Classroom
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class ToDoList(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)    


class UserQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    is_passed = models.BooleanField(default=False)
    date_passed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.quiz.quiz_name


class UserTest(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    is_passed = models.BooleanField(default=False)
    date_passed = models.DateField(null=True, blank=True)



class UserWord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    last_studied = models.DateTimeField(default=now)
    level = models.PositiveIntegerField(default=0)
    need_review = models.BooleanField(default=True)

    def check_review(self):
        if self.level == 0:
            self.need_review = True
        elif self.level == 1:
            if last_studied - datetime.now() < timedelta(days=1):
                self.need_review = True
        elif self.level == 2:
            if last_studied - datetime.now() < timedelta(days=2):
                self.need_review = True
        elif self.level == 3:
            if last_studied - datetime.now() < timedelta(days=4):
                self.need_review = True
        elif self.level == 4:
            if last_studied - datetime.now() < timedelta(days=8):
                self.need_review = True
        elif self.level == 5:
            if last_studied - datetime.now() < timedelta(days=14):
                self.need_review = True
        elif self.level > 5:
            self.need_review = False

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student(sender, instance, **kwargs):
    instance.student.save()
    todolist = ToDoList(user=instance.student)
    todolist.save()

