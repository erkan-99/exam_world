from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),


]
