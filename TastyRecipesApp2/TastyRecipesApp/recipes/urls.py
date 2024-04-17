from django.urls import path

from . import views
from .views import (
    CatalogueView,
    RecipeCreateView,
    RecipeDetailView,
    RecipeEditView,
    RecipeDeleteView,
)

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),  # Catalogue page
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),  # Recipe create page
    path('recipe/<int:recipe_id>/details/', RecipeDetailView.as_view(), name='recipe_details'),
    path('recipe/<int:recipe_id>/edit/', RecipeEditView.as_view(), name='recipe_edit'),
    path('recipe/<int:recipe_id>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
]
