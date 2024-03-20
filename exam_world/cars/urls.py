from django.urls import path, include
from . import views
urlpatterns = [
    path('catalogue/', views.catalogue_view, name='catalogue'),
    path('create/', views.create_car, name='create_car'),
    path('<int:pk>/', include([

        path('edit/', views.edit_car, name='edit-car'),
        path('delete/', views.car_delete, name='delete-car'),
        path('details/', views.car_details_view, name='car_details'),
    ]))
]
