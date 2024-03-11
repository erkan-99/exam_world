from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_car, name='create_car'),
    path('', views.catalogue_view, name='catalogue'),
    path('<int:car_id>/', views.car_details_view, name='car_details'),
    path('<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),
]

