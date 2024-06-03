from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form =  forms.taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task') 
    
    else:
        form =  forms.taskForm()
    return render(request, 'add_task.html', {'data' : form})