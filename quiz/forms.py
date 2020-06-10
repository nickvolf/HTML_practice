from django.forms import modelformset_factory
from django import forms
from .models import Quiz, ChooseWordQuestion, ChooseSentenceQuestion, PosNegQuestion, ResponseQuestion, MCImage


class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"


class SendQuizInfoForm(forms.Form):
    points = forms.CharField()


class CWQuestionForm(forms.ModelForm):
    class Meta:
        model = ChooseWordQuestion
        fields = "__all__"

class CSQuestionForm(forms.ModelForm):
    class Meta:
        model = ChooseSentenceQuestion
        fields = "__all__"

class PNQuestionForm(forms.ModelForm):
    class Meta:
        model = PosNegQuestion
        fields = "__all__"

class RPQuestionForm(forms.ModelForm):
    class Meta:
        model = ResponseQuestion
        fields = "__all__"

class MCImageForm(forms.ModelForm):
    class Meta:
        model = MCImage
        fields = "__all__"
