from django.db import models
# use uuid to generate unique randome ids
import uuid
# use country library for saving countries as ISO country codes
from django_countries.fields import CountryField
# relativedelta to calculate interval between two dates
from dateutil.relativedelta import relativedelta
from datetime import datetime


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
            )
    name = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        # Set the default plural name displayed in admin site
        verbose_name_plural = "categories"

    # Provide a more human readable object name
    def __str__(self):
        return "Category : {}".format(self.name)


class Business(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
            )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="category")
    name = models.CharField(max_length=20)
    registrationDate = models.DateTimeField()
    location = CountryField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        # get the interval of time in years between registration date of company to the current time
        return relativedelta(self.registrationDate, datetime.now()).years

    class Meta:
        verbose_name_plural = "businesses"

    # Provide a more human readable object name
    def __str__(self):
        return "Business : {}".format(self.name)
