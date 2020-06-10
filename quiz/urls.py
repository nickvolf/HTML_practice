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
    path('/take/<int:pk>/', views.quiz_take_view, name='quiz-take'),
    path('add/', views.quiz_create_view, name='quiz-create'),
    path('<int:pk>/update', QuizUpdateView.as_view(), name='quiz-update'),
    path('<int:pk>/delete', QuizDeleteView.as_view(), name='quiz-delete'),

    #questions
    path('upload_image/', views.upload_image, name='image-upload'),
    path('cwq/create/<int:pk>', views.create_cwq, name='cwq-create'),
    path('csq/create/<int:pk>', views.create_csq, name='csq-create'),
    path('pnq/create/<int:pk>', views.create_pnq, name='pnq-create'),
    path('rpq/create/<int:pk>', views.create_rpq, name='rpq-create'),
]
