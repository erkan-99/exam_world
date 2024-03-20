from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django import forms

from .forms import EditProfileForm, DeleteProfileForm
from .models import Profile
from ..cars.models import Car


def get_first_profile() -> object:
    return Profile.objects.first()


class ProfileCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password'
        }
        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreationForm()
    return render(request, 'profiles/profile-create.html', {'form': form})



def profile_delete(request):
    profile = get_first_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)


def profile_edit(request):

    profile = get_first_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)


def profile_details(request):
    profile = get_first_profile()
    total_sum = Car.objects\
        .filter(owner=profile, owner__isnull=False)\
        .aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        'profile': profile,
        'total_sum': total_sum
    }

    return render(request, template_name='profiles/profile-details.html', context=context)
