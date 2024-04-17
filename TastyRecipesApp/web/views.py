# web/views.py
from django.views.generic import TemplateView

from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.recipes.models import Recipe


class HomeView(TemplateView):
    template_name = 'web/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        recipes = Recipe.objects.all()  # Fetch all recipes (adjust query as needed)
        context['profile'] = profile
        context['recipes'] = recipes
        return context