from django.db import models
from django.core.exceptions import ValidationError


# Custom validator for ensuring the first letter is capital
def starts_with_capital_validator(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")


# Custom validator for ensuring the nickname length is at least 2 characters
def min_length_2_validator(value):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")


# Model for Profile
class Profile(models.Model):
    first_name = models.CharField(max_length=30, validators=[starts_with_capital_validator])
    last_name = models.CharField(max_length=30, validators=[starts_with_capital_validator])
    nickname = models.CharField(max_length=20, validators=[min_length_2_validator], unique=True,
                                error_messages={'unique': "Nickname must be unique!"})
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True)


