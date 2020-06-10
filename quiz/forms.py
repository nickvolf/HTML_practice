from django.forms import modelformset_factory
from django import forms
from .models import Quiz


class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"


class SendQuizInfoForm(forms.Form):
    points = forms.CharField()
