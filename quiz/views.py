from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Quiz, PosNegQuestion


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quizes.html'

class QuizView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"

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

class QuestionCreateView(CreateView):
    model = PosNegQuestion
    template_name = 'quiz/create_question.html'
    fields = ['image', 'correct_answer', 'wrong_asnwer1', 'points']
    success_url = reverse_lazy('home')
