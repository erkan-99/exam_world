from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    if len(username) < 3:
        raise ValidationError(_("Username must be at least 3 chars long!"))
    if not username.replace('_', '').isalnum():
        raise ValidationError(_("Username must contain only letters, digits, and underscores!"))


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[validate_username])
    email = models.EmailField()
    age = models.IntegerField(help_text="Age requirement: 21 years and above.", validators=[MinValueValidator(21)])
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)


@property
def full_name(self):
    if self.first_name and self.last_name:
        return f'{self.first_name} {self.last_name}'
    if self.first_name:
        return f'{self.first_name}'
    if self.last_name:
        return f'{self.last_name}'
    return None

