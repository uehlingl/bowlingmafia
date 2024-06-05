from django.db import models

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.
class BowlingCenter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    street_address = models.CharField(max_length=128, verbose_name='address')
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField(max_length=5)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=128, null=True, blank=True)
    website = models.URLField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.name} -- {self.city}, {self.state}'


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    bowling_centers = models.ManyToManyField(BowlingCenter, related_name='%(class)s_bowling_center')

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True