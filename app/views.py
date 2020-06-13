from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from users.models import CustomUser


def home_view(request):
    quiz_list = request.user.userquiz_set.filter(is_passed=False)
    return render(request, 'home.html', {"quiz_list": quiz_list})


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
