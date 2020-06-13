from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views


urlpatterns = [

    path('<int:pk>/', views.quiz_detail_view, name='quiz-detail'),
    path('take/<int:pk>/', views.quiz_take_view, name='quiz-take'),
    path('add/<int:pk>', views.quiz_create_view, name='quiz-create'),
    # path('<int:pk>/update', QuizUpdateView.as_view(), name='quiz-update'),
    path('<int:pk>/delete', views.quiz_delete_view, name='quiz-delete'),

    # create questions
    path('upload_image/', views.upload_image, name='image-upload'),
    path('cwq/create/<int:pk>', views.create_cwq, name='cwq-create'),
    path('csq/create/<int:pk>', views.create_csq, name='csq-create'),
    path('pnq/create/<int:pk>', views.create_pnq, name='pnq-create'),
    path('rpq/create/<int:pk>', views.create_rpq, name='rpq-create'),
    path('word/create/<int:pk>', views.word_create_view, name='word-create'),

    # delete questions
    path('cwq/delete/<int:pk>', views.cwq_delete_view, name='cwq-delete'),
    path('csq/delete/<int:pk>', views.csq_delete_view, name='csq-delete'),
    path('pnq/delete/<int:pk>', views.pnq_delete_view, name='pnq-delete'),
    path('rpq/delete/<int:pk>', views.rpq_delete_view, name='rpq-delete'),
    path('word/delete/<int:pk>', views.word_delete_view, name='word-delete'),

    # detail question
    path('cwq/detail/<int:pk>', views.detail_cwq, name='cwq-detail'),
    path('csq/detail/<int:pk>', views.detail_csq, name='csq-detail'),
    path('pnq/detail/<int:pk>', views.detail_pnq, name='pnq-detail'),
    path('rpq/detail/<int:pk>', views.detail_rpq, name='rpq-detail'),
]
