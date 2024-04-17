from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from TastyRecipesApp.profiles.forms import ProfileCreationForm, ProfileEditForm
from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.recipes.models import Recipe


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')  # Redirect to catalogue page after profile creation    pass


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'  # Specify the template name for the profile detail page

    def get_object(self, queryset=None):
        # Fetch the profile based on some predefined logic
        # For example, you could fetch the first profile in the database
        return Profile.objects.first()

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm  # Use the ProfileEditForm for the form
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        # Fetch the profile based on some predefined logic
        # For example, you could fetch the first profile in the database
        return Profile.objects.first()




def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        Recipe.objects.all().delete()
        return redirect('home')
    else:
        profile = Profile.objects.first()  # Fetch the profile object
        return render(request, 'profiles/delete-profile.html', {'profile': profile})

