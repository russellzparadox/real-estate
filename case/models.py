from django.db import models
from land.models import Land


# Create your models here.

class Case(models.Model):
    title = models.CharField(max_length=255)
    land = models.OneToOneField(Land, on_delete=models.CASCADE)
    content = models.TextField()
    sellPrice = models.PositiveBigIntegerField()
    rentPrice = models.PositiveBigIntegerField()
