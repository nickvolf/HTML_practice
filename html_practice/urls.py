from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('app.urls')),
    path('quiz/', include('quiz.urls')),
    path('books/', include('books.urls')),
    path('classroom/', include('classroom.urls')),
    path('signup/', user_views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
