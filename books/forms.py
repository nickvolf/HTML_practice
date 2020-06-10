from django.forms import modelformset_factory
from django import forms
from .models import Book, Unit


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class UnitCreateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

