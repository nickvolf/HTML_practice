from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book-list'),
    path('<int:pk>/', views.book_detail_view, name='book-detail'),
    path('add/', views.book_create_view, name='book-add'),
    path('<int:pk>/update', views.book_update_view, name='book-update'),
    path('<int:pk>/delete', views.book_delete_view, name='book-delete'),
]