from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import SendQuizInfoForm, QuizCreateForm, CWQuestionForm, CSQuestionForm, RPQuestionForm, PNQuestionForm, MCImageForm
import datetime

from .models import Quiz


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quizzes.html'


def quiz_detail_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, "quiz/quiz_detail.html", {"quiz": quiz})


def quiz_take_view(request, pk):
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
        return render(request, 'quiz/quiz_take.html', {"quiz": quiz, "return_form": return_form})


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


def create_cwq(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = CWQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('quiz-detail', pk=pk)
    else:
        form = CWQuestionForm()
        form.fields['quiz'].initial = quiz
        return render(request, 'quiz/quiz_create.html', {"form": form})


def create_csq(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = CSQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('quiz-detail', pk=pk)
    else:
        form = CSQuestionForm()
        form.fields['quiz'].initial = quiz
        return render(request, 'quiz/quiz_create.html', {"form": form})


def create_pnq(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = PNQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('quiz-detail', pk=pk)
    else:
        form = PNQuestionForm()
        form.fields['quiz'].initial = quiz
        return render(request, 'quiz/quiz_create.html', {"form": form})


def create_rpq(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = RPQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('quiz-detail', pk=pk)
    else:
        form = RPQuestionForm()
        form.fields['quiz'].initial = quiz
        return render(request, 'quiz/quiz_create.html', {"form": form})

def upload_image(request):
    if request.method == "POST":
        form = MCImageForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('book-list')
    else:
        form = MCImageForm()
        return render(request, 'quiz/quiz_create.html', {"form": form})


