
from django.shortcuts import render,redirect
from add_task_app.models import taskModel
from category_app.models import categoryModel
from add_task_app.forms import taskForm

def show_task(request):
    tasks = taskModel.objects.all()
    categories = categoryModel.objects.all()

    
    combined_data = []
    for task in tasks:
        task_categories = [category.category_name for category in task.categorymodel_set.all()]
        combined_data.append({
            'task': task,
            'categories': task_categories
        })

    context = {
        'combined_data': combined_data
    }

    return render(request, 'show.html', context)



def edit_task(request,id):
    edit = taskModel.objects.get(pk=id)
    form = taskForm(instance = edit)
    if request.method == 'POST':
        form = taskForm(  request.POST ,instance=edit  )
        if form.is_valid():
            form.save()
            return redirect('add_task') 
    
    
    return render(request, 'add_task.html', {'data' : form})
    

def delete(request, id):
     edit = taskModel.objects.get(pk=id)
     edit.delete()
     return redirect('show_task')