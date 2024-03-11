from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



from django import forms
from .models import Profile


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
            return redirect('index')
    else:
        form = ProfileCreationForm()
    return render(request, 'profiles/profile-create.html', {'form': form})



@login_required
def profile_delete(request):
    if request.method == 'POST':
        (request.user.delete())
        return redirect('index')  # Redirect to the index page after deletion
    return render(request, 'profiles/profile-delete.html')


@login_required
def profile_delete(request):
    if request.method == 'POST':
        # Delete the profile and associated cars
        request.user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('index')  # Redirect to the index page after deletion
    return render(request, 'profiles/profile-delete.html')