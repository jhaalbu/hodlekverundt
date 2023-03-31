from django.db import models

# Create your models here.
class Rute(models.Model):
    tittel = models.CharField(max_length=100)
    skildring = models.TextField()
    lengde = models.FloatField()
    image = models.CharField(max_length=100)