from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():

            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('catalogue')  # Redirect to the Catalogue page
    else:
        form = CarForm()
    return render(request, 'cars/car-create.html', {'form': form})


def catalogue_view(request):
    cars = Car.objects.all()
    return render(request, 'cars/catalogue.html', {'cars': cars})


def car_details_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car-details.html', {'car': car})



def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')  # Redirect to catalogue page after successful edit
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car-edit.html', {'form': form})



def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')  # Redirect to the catalogue page after deletion
    return render(request, 'cars/car-delete.html', {'car': car})