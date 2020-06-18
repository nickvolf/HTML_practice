from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    # Book Paths
    path('<int:pk>', views.class_detail_view, name='class-detail'),
    path('list/', views.class_list_view, name='class-list'),
    path('add_student/<int:pk>/', views.class_add_students, name='add-student'),
    path('remove_student/<int:pk>/', views.class_remove_students, name='remove-student'),
    path('add_book/<int:pk>/', views.class_add_books, name='add-book'),
    path('remove_book/<int:pk>/', views.class_remove_books, name='remove-book'),

    path('create/', views.add_class_view, name='class-create')
]