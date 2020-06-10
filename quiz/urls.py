from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from .views import (
    QuizUpdateView,
    QuizDeleteView,
    QuizListView, )

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<int:pk>/', views.quiz_detail_view, name='quiz-detail'),
    path('add/', views.quiz_create_view, name='quiz-create'),
    path('<int:pk>/update', QuizUpdateView.as_view(), name='quiz-update'),
    path('<int:pk>/delete', QuizDeleteView.as_view(), name='quiz-delete'),

]
