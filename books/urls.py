from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    # Book Paths
    path('', views.book_list_view, name='book-list'),
    path('<int:pk>/', views.book_detail_view, name='book-detail'),
    path('add/', views.book_create_view, name='book-create'),
    path('<int:pk>/update', views.book_update_view, name='book-update'),
    path('<int:pk>/delete', views.book_delete_view, name='book-delete'),

    # Unit Paths
    path('unit/<int:pk>/', views.unit_detail_view, name='unit-detail'),
    path('unit/add/<int:pk>', views.unit_create_view, name='unit-create'),
    path('unit/<int:pk>/update', views.unit_update_view, name='unit-update'),
    path('unit/<int:pk>/delete', views.unit_delete_view, name='unit-delete'),

]