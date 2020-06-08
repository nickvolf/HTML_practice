from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
import json
from django.core.serializers import serialize

from .models import Quiz


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quizes.html'


def quiz_detail_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    choose_word_questions = quiz.choosewordquestion_set.all()
    cwq_list = serialize("json", quiz.choosewordquestion_set.all())

    return render(request, 'quiz/quiz_detail.html', {"quiz":quiz, "cwq_list":cwq_list})

class QuizCreateView(CreateView):
    model = Quiz
    template_name = 'quiz/quiz_create.html'
    fields = ['quiz_name', 'quiz_display_name']

class QuizUpdateView(UpdateView):
    model = Quiz
    template_name = 'quiz/quiz_edit.html'
    fields = ['quiz_name', 'quiz_display_name']

class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz/quiz_delete.html'
    success_url = reverse_lazy('quiz-list')
