from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from app.views import GradesView, TodoView, JavaView, AjaxView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('grades/', login_required(GradesView.as_view()), name='grades'),
    path('todo/', login_required(TodoView.as_view()), name='todo'),
    path('js/', JavaView.as_view(), name='js'),
    path('ajax/', AjaxView.as_view(), name='ajax1'),
]
