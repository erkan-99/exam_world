from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("exam_world.web.urls")),
    path("profile/", include("exam_world.profiles.urls")),
    path("car/", include("exam_world.cars.urls")),
]
