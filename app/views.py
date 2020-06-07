from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from quiz.models import Quiz


class IndexView(ListView):
    model = Quiz
    template_name='home.html'
    paginate_by = 4


class GradesView(TemplateView):
    template_name='grades.html'

class TodoView(TemplateView):
    template_name='todo.html'

class ClassroomView(TemplateView):
    template_name='classroom.html'

class SignUpView(CreateView):
    template_name = 'base.html'
    form_class = UserCreationForm

class JavaView(TemplateView):
    template_name = 'javascript.html'

class AjaxView(TemplateView):
    template_name = 'ajax1.html'
