from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from exam_world.profiles.models import Profile


def index(request):
    user_has_profile = Profile.objects.filter(user=request.user).exists() if request.user.is_authenticated else False

    return render(request, 'web/index.html', {'user_has_profile': user_has_profile})
