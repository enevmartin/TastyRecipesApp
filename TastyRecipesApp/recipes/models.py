from django.core.exceptions import ValidationError
from django.db import models

from TastyRecipesApp.profiles.models import Profile


class Recipe(models.Model):
    CUISINE_CHOICES = [
        ('FR', 'French'),
        ('CN', 'Chinese'),
        ('IT', 'Italian'),
        ('BA', 'Balkan'),
        ('OT', 'Other'),
    ]

    title = models.CharField(max_length=100, unique=True, error_messages={'unique': "We already have a recipe with "
                                                                                    "the same title!"})
    cuisine_type = models.CharField(max_length=7, choices=CUISINE_CHOICES)
    ingredients = models.TextField(help_text="Ingredients must be separated by a comma and space.")
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Provide the cooking time in minutes")
    image_url = models.URLField(blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes')

    # Override the clean method to ensure cooking time is at least 1
    def clean(self):
        if self.cooking_time < 1:
            raise ValidationError("Cooking time must be at least 1 minute")
