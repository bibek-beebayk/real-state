from tabnanny import verbose
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


PROPERTY_TYPE_CHOICES = [
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Room', 'Room'),
    ('Flat', 'Flat'),
    ('Land', 'Land'),
    ('Other', 'Other'),
]

CONTRACT_TYPE_CHOICES = [
    ('Rent', 'Rent'),
    ('Sale', 'Sale'),
    ('Lease', 'Lease'),
    ('Other', 'Other'),
]


class Amenity(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    icon = VersatileImageField(upload_to='amenities', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Amenities'


class Property(models.Model):
    property_code = models.CharField(max_length=16, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    property_type = models.CharField(
        max_length=255, choices=PROPERTY_TYPE_CHOICES)
    contract_type = models.CharField(
        max_length=255, choices=CONTRACT_TYPE_CHOICES)
    listed_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_negotiable = models.BooleanField(default=False)
    listed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='properties')
    description = RichTextField()
    bedroom = models.IntegerField(blank=True, null=True)
    bathroom = models.IntegerField(blank=True, null=True)
    kitchen = models.IntegerField(blank=True, null=True)
    parking = models.IntegerField(blank=True, null=True)
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-listed_at']
        verbose_name_plural = 'Properties'


class PropertyImage(models.Model):
    image = VersatileImageField(upload_to='property_images')
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='images')

    SIZES = {
        'image': {
            'thumbnail': 'thumbnail__640x360',
        }
    }


class Facility(models.Model):
    title = models.CharField(
        max_length=100, help_text='Eg. Property face, area, road-width, road-type, etc.')
    value = models.CharField(
        max_length=100, help_text='Eg. North, 1000 sqft, 20 ft, tar, etc.')
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Facilities'
