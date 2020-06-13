from django.db import models
from django.utils.timezone import now
from classroom.models import Classroom


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(default=now, editable=False)
    classroom = models.ManyToManyField(Classroom, blank=True)

    def __str__(self):
        return self.title


class Unit(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.number) + ": " + str(self.title)
