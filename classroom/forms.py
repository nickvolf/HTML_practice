from django import forms
from .models import Classroom
from django.shortcuts import get_list_or_404
from users.models import Student
from books.models import Book


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'


class AddStudent(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.filter(has_class=False))


class RemoveStudent(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.filter(has_class=True))


class AddBook(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())


class RemoveBook(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())