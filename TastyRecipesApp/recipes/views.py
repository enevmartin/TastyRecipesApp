from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.recipes import forms
from TastyRecipesApp.recipes.forms import RecipeCreationForm
from TastyRecipesApp.recipes.models import Recipe




class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreationForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        # Assign the author of the recipe to the first profile object in the database
        form.instance.author = Profile.objects.first()
        return super().form_valid(form)


# def create_recipe(request):
#     if request.method == 'POST':
#         form = forms.RecipeCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#     else:
#         form = forms.RecipeCreationForm()
#
#     context = {'form': form}
#
#     return render(request, template_name='recipes/create-recipe.html', context=context)


class CatalogueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'  # Specify the template name for the catalogue page
    context_object_name = 'recipes'  # Specify the context variable name to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()  # Get the first profile object
        context['profile'] = profile  # Add profile object to the context
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'  # Specify the template name for the recipe detail page
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()  # Get the first profile object
        context['profile'] = profile  # Add profile object to the context
        return context
class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeCreationForm
    template_name = 'recipes/edit-recipe.html'  # Specify the template name for the recipe edit page
    success_url = reverse_lazy('catalogue')  # Redirect to catalogue page after editing recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()  # Get the first profile object
        context['profile'] = profile  # Add profile object to the context
        return context


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/delete-recipe.html'  # Specify the template name for the recipe delete page
    success_url = reverse_lazy('catalogue')  # Redirect to catalogue page after deleting recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()  # Get the first profile object
        context['profile'] = profile  # Add profile object to the context
        return context