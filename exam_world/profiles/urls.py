from django.urls import path

from exam_world.profiles import views

urlpatterns = [
    path('create/', views.create_profile, name='create-profile'),
    path('edit/', views.profile_edit, name='edit-profile'),
    path('delete/', views.profile_delete, name='delete-profile'),
    path('details/', views.profile_details, name='profile-details'),

]
