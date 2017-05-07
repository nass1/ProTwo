from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email    = models.EmailField(max_length=254)

    def __str__(self):
        return self.firstname
