from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from datetime import datetime, timedelta
from users.models import Student, ToDoList
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    user = request.user
    if hasattr(user, 'todolist'):
        quiz_list = user.todolist.userquiz_set.filter(is_passed=False)
        if hasattr(user.todolist, 'wordlist'):
            for word in user.todolist.wordlist.userword_set.all():
                word.check_review()
        else:
            wordlist = WordList(todo=user.todolist)
            wordlist.save()
            for word in user.todolist.wordlist.userword_set.all():
                word.check_review()

    else:
        todolist = ToDoList(user=user)
        todolist.save()
        quiz_list = user.todolist.userquiz_set.filter(is_passed=False)
    streak = user.streak
    if streak == 1:
        streak_text = "1 day"
    else:
        streak_text = f'{streak} days'
    return render(request, 'home.html', {"quiz_list": quiz_list, "streak": streak_text})


class GradesView(TemplateView):
    template_name = 'grades.html'


class TodoView(TemplateView):
    template_name = 'todo.html'


class SignUpView(CreateView):
    template_name = 'base.html'
    form_class = UserCreationForm


class JavaView(TemplateView):
    template_name = 'javascript.html'


class AjaxView(TemplateView):
    template_name = 'ajax1.html'
