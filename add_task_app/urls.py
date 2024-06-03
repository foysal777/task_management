
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-task/' , views.add_task , name= 'add_task' ),
]
