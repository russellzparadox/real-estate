from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def land_upload_path(instance, filename):
    return f'land{instance.id}/{filename}'


class Feature(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Land(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    address = models.CharField(max_length=750)
    areaOfBuilding = models.FloatField()
    areaOfBuilding = models.FloatField(blank=True, null=True)
    areaOfLand = models.FloatField()
    electricityAmper = models.FloatField(blank=True, null=True)
    edari = models.CharField(max_length=255, blank=True, null=True)
    buildingHeight = models.FloatField(blank=True, null=True)
    phoneNumber = PhoneNumberField()
    secondaryPhoneNumber = PhoneNumberField()
    ownerName = models.CharField(max_length=255)
    image = models.ImageField(upload_to=land_upload_path, blank=True, null=True)

    features = models.ManyToManyField(Feature, related_name='lands', blank=True, null=True)

    privetNote = models.TextField(blank=True, null=True)
