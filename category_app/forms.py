from django import forms
from category_app.models import categoryModel

class categoryForm(forms.ModelForm):
    class Meta:
        model = categoryModel
        fields ='__all__'
        