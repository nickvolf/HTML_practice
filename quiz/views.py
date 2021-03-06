from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendQuizInfoForm, QuizCreateForm, CWQuestionForm, CSQuestionForm, RPQuestionForm, PNQuestionForm, \
    MCImageForm, WordForm
import datetime

from .models import Quiz, ChooseWordQuestion, ChooseSentenceQuestion, PosNegQuestion, ResponseQuestion, Word
from books.models import Unit
from users.models import UserQuiz, UserWord, ToDoList
from datetime import datetime, timedelta, date 


def check_current_streak(user):
    total_streak = 0
    current_streak = 0
    today = date.today()
    compareDate = today + timedelta(1) #tomorrow
    # Using list() here pulls all the quizzes
    # Gets all the dates for the todolist whose date is today
    if hasattr(user, 'todolist'):
        passed_dates = list(user.todolist.userquiz_set.values("date_passed").filter(date__lte = today).order_by("-date_passed"))
    else:
        todolist = ToDoList(user=user)
        todolist.save()
        passed_dates = list(user.todolist.userquiz_set.values("date_passed").filter(date__lte = today).order_by("-date_passed"))

                
    for pass_date in passed_dates:
        #Get the difference between the dates
        delta = compareDate - pass_date

        if delta.days == 1: #Keep the streak going
            current_streak +=1
        elif delta.days == 0: # Don't bother increasing the day.
            pass
        else:
            break

        compareDate = date_passed

    if current_streak > total_streak:
        total_streak = current_streak

    return total_streak


def quiz_detail_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, "quiz/quiz_detail.html", {"quiz": quiz})


def quiz_take_view(request, pk):
    student = request.user.student
    quiz = Quiz.objects.get(pk=pk)
    if request.method == "POST":
        form = SendQuizInfoForm(request.POST)
        if form.is_valid():
            points = form.cleaned_data['points']
            student.score = student.score + int(points)
            word_set = quiz.word_set.all()
            userquiz = student.todolist.userquiz_set.get(quiz=quiz)
            userquiz.is_passed = True
            userquiz.date_passed = datetime.now()
            userquiz.save()
            for word in word_set:
                if word not in student.words.all():
                    student.words.add(word)
            student.last_test = datetime.now()
            student.streak = check_current_streak(student)
            student.save()

        return redirect('home')

    else:
        return_form = SendQuizInfoForm()
        quiz = get_object_or_404(Quiz, pk=pk)
        return render(request, 'quiz/quiz_take.html', {"quiz": quiz, "return_form": return_form})


def quiz_create_view(request, pk):
    if request.method == "POST":
        form = QuizCreateForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            book = quiz.unit.book
            for classroom in book.classroom.all():
                for student in classroom.customuser_set.all():
                    if hasattr(student, 'todolist'):
                        userquiz = UserQuiz(quiz=quiz, user=student, todolist=user.todolist)
                        userquiz.save()
                    else:
                        todolist = ToDoList(user = student)
                        todolist.save()

            return redirect('unit-detail', pk=quiz.unit.pk)
    else:
        unit = get_object_or_404(Unit, pk=pk)
        form = QuizCreateForm()
        form.fields['unit'].initial = unit
        return render(request, 'quiz/quiz_create.html', {"form": form})


def quiz_delete_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    unit = quiz.unit
    if request.method == "POST":
        quiz.delete()
        return redirect('unit-detail', unit.pk)
    else:
        return render(request, 'quiz/quiz_delete.html', {"quiz": quiz})


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


def detail_cwq(request, pk):
    question = get_object_or_404(ChooseWordQuestion, pk=pk)
    image = question.image
    return render(request, "quiz/cwq.html", {'question': question, "image": image})


def cwq_delete_view(request, pk):
    question = get_object_or_404(ChooseWordQuestion, pk=pk)
    quiz = question.quiz
    if request.method == "POST":
        question.delete()
        return redirect('quiz-detail', quiz.pk)
    else:
        return render(request, 'quiz/question_delete.html')


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


def detail_csq(request, pk):
    question = get_object_or_404(ChooseSentenceQuestion, pk=pk)
    return render(request, "quiz/csq.html", {'question': question})


def csq_delete_view(request, pk):
    question = get_object_or_404(ChooseSentenceQuestion, pk=pk)
    quiz = question.quiz
    if request.method == "POST":
        question.delete()
        return redirect('quiz-detail', quiz.pk)
    else:
        return render(request, 'quiz/question_delete.html')


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


def detail_pnq(request, pk):
    question = get_object_or_404(PosNegQuestion, pk=pk)
    return render(request, "quiz/pnq.html", {'question': question})


def pnq_delete_view(request, pk):
    question = get_object_or_404(PosNegQuestion, pk=pk)
    quiz = question.quiz
    if request.method == "POST":
        question.delete()
        return redirect('quiz-detail', quiz.pk)
    else:
        return render(request, 'quiz/question_delete.html')


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


def detail_rpq(request, pk):
    question = get_object_or_404(ResponseQuestion, pk=pk)
    return render(request, "quiz/rpq.html", {'question': question})


def rpq_delete_view(request, pk):
    question = get_object_or_404(ResponseQuestion, pk=pk)
    quiz = question.quiz
    if request.method == "POST":
        question.delete()
        return redirect('quiz-detail', quiz.pk)
    else:
        return render(request, 'quiz/question_delete.html')


def word_create_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save()
            return redirect("quiz-detail", pk=word.quiz.pk)

    else:
        form = WordForm()
        form.fields['quiz'].initial = quiz
        return render(request, 'quiz/create_question.html', {"form": form})


def word_delete_view(request, pk):
    question = get_object_or_404(Word, pk=pk)
    quiz = question.quiz
    if request.method == "POST":
        question.delete()
        return redirect('quiz-detail', quiz.pk)
    else:
        return render(request, 'quiz/question_delete.html')


def upload_image(request):
    if request.method == "POST":
        form = MCImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('book-list')
        else:
            return redirect('home')

    else:
        form = MCImageForm()
        return render(request, 'quiz/image_upload.html', {"form": form})
