from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from .views import (
    QuizView,
    QuizCreateView,
    QuizUpdateView,
    QuizDeleteView,
    QuizListView,
    QuestionCreateView,    )


urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<int:pk>/', views.quiz_detail_view, name='quiz-detail'),
    path('add/', QuizCreateView.as_view(), name='quiz-add'),
    path('<int:pk>/update', QuizUpdateView.as_view(), name='quiz-update'),
    path('<int:pk>/delete', QuizDeleteView.as_view(), name='quiz-delete'),
    path('add/question/', QuestionCreateView.as_view(), name='question-add'),

]
