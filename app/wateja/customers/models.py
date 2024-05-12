from django.db import models
# import uuid package to use randome 128 bits objects as ids
# replaces the default sequential id
import uuid
# import the business model
from business.models import Business
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
            )
    business = models.ForeignKey(
            Business,
            on_delete=models.CASCADE
            )
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(blank=True)
    dateOfBirth = models.DateTimeField()
    nationality = CountryField()
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
