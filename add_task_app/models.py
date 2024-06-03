from django.db import models

# Create your models here.
class taskModel(models.Model):
    task_id = models.AutoField(primary_key=True )
    task_tittle = models.CharField(max_length=50)
    task_des = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.task_tittle
    