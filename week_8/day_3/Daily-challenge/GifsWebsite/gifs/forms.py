from django import forms
from .models import GifModel,Category
    
class GifModelForm(forms.ModelForm):
    class Meta:
        model = GifModel
        fields = ['title','url','category']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']