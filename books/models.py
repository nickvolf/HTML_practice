from django.db import models
from django.utils.timezone import now


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title


class Unit(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.number) + ": " + str(self.title)
