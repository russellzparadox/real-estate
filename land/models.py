from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def land_upload_path(instance, filename):
    return f'land{instance.id}/{filename}'


# Create your models here.
class Land(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    address = models.CharField(max_length=750)
    areaOfBuilding = models.FloatField()
    areaOfLand = models.FloatField()
    electricityAmper = models.FloatField()
    edari = models.CharField(max_length=255)
    buildingHeight = models.FloatField()
    phoneNumber = PhoneNumberField()
    secondaryPhoneNumber = PhoneNumberField()
    ownerName = models.CharField(max_length=255)
    image = models.ImageField(upload_to=land_upload_path)

    water = models.BooleanField(default=False)
    oghaf = models.BooleanField(default=False)
    bascule60Ton = models.BooleanField(default=False)
    phoneLine = models.BooleanField(default=False)
    crane20Ton = models.BooleanField(default=False)
    crane5Ton = models.BooleanField(default=False)
    crane40Ton = models.BooleanField(default=False)
    waterWheel = models.BooleanField(default=False)
    fullTitle = models.BooleanField(default=False)  # سند شیش دنگ
    solhGhati = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    g60Gas = models.BooleanField(default=False)
    proxy = models.BooleanField(default=False)  # وکالتی
    elevator = models.BooleanField(default=False)
    ethernet = models.BooleanField(default=False)
    lift5Ton = models.BooleanField(default=False)
    crane10Ton = models.BooleanField(default=False)
    crane4Ton = models.BooleanField(default=False)
    crane7Ton = models.BooleanField(default=False)
    roofCrane = models.BooleanField(default=False)
    daftarcheShahrak = models.BooleanField(default=False)  # این چه بولشیتیه
    commonTitle = models.BooleanField(default=False)  # سند مشاع
    memorandum = models.BooleanField(default=False)  # قولنامه
    gas2Pound = models.BooleanField(default=False)  # گاز دو پوند
    newBuild = models.BooleanField(default=False)

    privetNote = models.TextField()
