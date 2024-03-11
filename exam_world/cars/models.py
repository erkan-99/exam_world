from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from exam_world.profiles.models import Profile


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    model = models.CharField(max_length=15)
    year = models.IntegerField(validators=[MinValueValidator(1999), MaxValueValidator(2030)])
    image_url = models.URLField(unique=True, error_messages={'unique': "This image URL is already in use! Provide a new one."})
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cars')  # Use the Profile model directly

    def clean(self):
        if not (1999 <= self.year <= 2030):
            raise ValidationError("Year must be between 1999 and 2030!")
