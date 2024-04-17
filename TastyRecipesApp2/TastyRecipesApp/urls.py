from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('TastyRecipesApp.web.urls')),  # Include web app urls
    path('recipe/', include('TastyRecipesApp.recipes.urls')),  # Include recipes app urls
    path('profile/', include('TastyRecipesApp.profiles.urls')),  # Include profiles app urls
    path('admin/', admin.site.urls),
]
