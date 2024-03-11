from django.urls import path

from exam_world.web.views import index

urlpatterns = (
    path('', index, name='index'),
)