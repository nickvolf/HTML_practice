from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from datetime import datetime, timedelta
from users.models import CustomUser


def home_view(request):
    user = request.user
    quiz_list = request.user.userquiz_set.filter(is_passed=False)
    streak = current_streak(user)
    if streak == 1:
        streak_text = "1 day"
    else:
        streak_text = f'{streak} days'
    return render(request, 'home.html', {"quiz_list": quiz_list, "streak": streak_text})


def current_streak(user):
    quiz_list = user.userquiz_set.filter(is_passed=True).order_by('-date_passed')
    if quiz_list.count() > 0:
        
        last_test = quiz_list.first()
        if datetime.now().date() - last_test.date_passed > timedelta(1):
            user.streak = 0
        else:
            user.streak = 1
            for test in quiz_list:
                pass

        user.save()
    return user.streak


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
