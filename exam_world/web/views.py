from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from exam_world.profiles.models import Profile
from exam_world.profiles.views import get_first_profile


def index(request):
    profile = get_first_profile()
    context = {'profile': profile}

    return render(request, template_name='web/index.html', context=context)
