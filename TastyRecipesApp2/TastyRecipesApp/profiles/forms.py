# profiles/forms.py
from django import forms
from .models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef', 'bio']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef', 'bio']
        labels = {
            'nickname': 'Nickname',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'chef': 'Chef',
            'bio': 'Bio'  # Label for the bio field
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4})  # Customize the textarea widget for the bio field
        }
