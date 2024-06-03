
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name= 'homepage'),
    path('addTask/' , include('add_task_app.urls')),
    path('category_app/' , include('category_app.urls')),
    path('show_app/' , include('show_app.urls')),
]
