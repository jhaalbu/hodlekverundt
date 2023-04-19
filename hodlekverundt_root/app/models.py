from django.db import models


# Create your models here.
class Info(models.Model):
    tittel = models.CharField(max_length=100)
    generell_info = models.TextField()

class Tekst(models.Model):
    tittel = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    image = models.CharField(max_length=100)

class Nyheter(models.Model):
    tittel = models.CharField(max_length=100)
    tekst = models.TextField()
    image = models.CharField(max_length=100)