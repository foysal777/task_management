from django.db import models
from add_task_app.models import taskModel 

# Create your models here.
class categoryModel(models.Model):
    category_name = models.CharField(max_length=20)
    task_model = models.ManyToManyField(taskModel) # you can merge the category name instead of task_model
    
    
    def __str__(self):
        return self.category_name
    