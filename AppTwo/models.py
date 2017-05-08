from django.db import models
from django.core.exceptions import ValidationError

def validate_even(value):
    try:
        check = User.objects.get(email=value)
        if check == value:
            raise ValidationError("Email already exisits")
    except:
        pass


class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email  = models.EmailField(max_length=254, unique=True, validators=[validate_even])

    def __str__(self):
        return self.firstname

