
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_task/', views.show_task , name= 'show_task'),
    path('edit_task/<int:id>', views.edit_task , name= 'edit_task'),
    path('delete/<int:id>', views.delete , name= 'delete'),
]
