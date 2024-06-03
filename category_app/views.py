from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def category(request):
    if request.method == 'POST':
        form =  forms.categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category') 
    
    else:
        form =  forms.categoryForm()
    return render(request, 'category.html', {'data' : form})
    
    
    