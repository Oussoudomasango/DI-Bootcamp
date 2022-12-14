from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phoneNumber = PhoneNumberField(blank=True, help_text='Contact phone number')
    adresse = models.CharField(max_length=30)
