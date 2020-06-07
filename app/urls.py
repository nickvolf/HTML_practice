from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from app.views import IndexView, GradesView, ClassroomView, TodoView, JavaView, AjaxView

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='home'),
    path('grades/', login_required(GradesView.as_view()), name='grades'),
    path('classroom/', login_required(ClassroomView.as_view()), name='classroom'),
    path('todo/', login_required(TodoView.as_view()), name='todo'),
    path('js/', JavaView.as_view(), name='js'),
    path('ajax/', AjaxView.as_view(), name='ajax1'),
]
