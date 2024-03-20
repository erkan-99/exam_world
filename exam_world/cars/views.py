

from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from .forms import DeleteCarForm
from .models import Car
from ..profiles.views import get_first_profile


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


def create_car(request):
    form = CarForm(request.POST or None)
    profile = get_first_profile()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='cars/car-create.html', context=context)


def catalogue_view(request):
    cars = Car.objects.all()
    context = {
        'profile': get_first_profile(),
        'cars': cars
    }

    return render(request, template_name='cars/catalogue.html', context=context)



def car_details_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'profile': get_first_profile(),
        'car': car
    }

    return render(request, template_name='cars/car-details.html', context=context)


def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
        'profile': get_first_profile(),
    }
    return render(request, 'cars/car-edit.html', context)




def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)
    context = {
        'profile': get_first_profile(),
        'form': form
    }

    return render(request, 'cars/car-delete.html', context)
