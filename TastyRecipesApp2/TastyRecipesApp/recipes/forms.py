# recipes/forms.py
from django import forms
from .models import Recipe

class RecipeCreationForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        widgets = {
            'ingredients': forms.TextInput(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Optional image URL here...'}),
        }




class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'cuisine_type': forms.TextInput(attrs={'readonly': 'readonly'}),
            'ingredients': forms.TextInput(attrs={'readonly': 'readonly'}),
            'instructions': forms.Textarea(attrs={'readonly': 'readonly'}),
            'cooking_time': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


