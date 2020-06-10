from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import SendQuizInfoForm, QuizCreateForm
import datetime

from .models import Quiz


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quizes.html'


def quiz_detail_view(request, pk):
    if request.method == "POST":
        form = SendQuizInfoForm(request.POST)
        if form.is_valid():
            points = form.cleaned_data['points']
            user = request.user
            user.score = user.score + int(points)
            quiz = Quiz.objects.get(pk=pk)
            word_set = quiz.word_set.all()
            for word in word_set:
                if word not in user.words.all():
                    user.words.add(word)
            user.last_test = datetime.datetime.now()
            user.save()

        return redirect('home')

    else:
        return_form = SendQuizInfoForm()
        quiz = get_object_or_404(Quiz, pk=pk)
        return render(request, 'quiz/quiz_detail.html', {"quiz": quiz, "return_form": return_form})


def quiz_create_view(request):
    if request.method == "POST":
        form = QuizCreateForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('unit-detail', pk=quiz.unit.pk)
    else:
        form = QuizCreateForm()
        return render(request, 'quiz/quiz_create.html', {"form": form})


class QuizUpdateView(UpdateView):
    model = Quiz
    template_name = 'quiz/quiz_edit.html'
    fields = ['quiz_name', 'quiz_display_name']


class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz/quiz_delete.html'
    success_url = reverse_lazy('quiz-list')
