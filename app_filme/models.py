from django.db import models


class Usuario (models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
# Create your models here.
