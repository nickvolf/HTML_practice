from django.forms import modelformset_factory
from django import forms
from .models import Quiz


class QuizCreateForm(forms.Form):
    quiz_name = forms.CharField(label='Quiz Name', max_length=30)
