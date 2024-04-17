from django.urls import path

from . import views
from .views import (
    ProfileCreateView,
    ProfileDetailView,
    ProfileEditView,
    # ProfileDeleteView,
)

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),  # Profile create page
    path('details/', ProfileDetailView.as_view(), name='profile_details'),  # Profile details page
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),  # Profile edit page
    path('delete/', views.delete_profile, name='profile_delete'),  # Profile delete page
]
